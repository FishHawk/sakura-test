from typing import List
import time
import requests

CARD = "A100"
HOST = "192.168.1.162:5002"
URI = f"http://{HOST}/api/v1/generate"

# A100 4bit :5002
# 3090 4bit :5000


def translate(line: List[str]):
    prompt = "<reserved_106>将下面的日文文本翻译成中文：{text}<reserved_107>".format(
        text="\n".join(line)
    )
    request = {
        "prompt": prompt,
        "auto_max_new_tokens": False,
        "max_tokens_second": 0,
        # Generation params. If 'preset' is set to different than 'None', the values
        # in presets/preset-name.yaml are used instead of the individual numbers.
        "preset": "None",
        "max_new_tokens": 1024,
        "do_sample": True,
        "temperature": 1.0,
        "top_p": 0.5,
        "repetition_penalty": 1.0,
        "num_beams": 1,
        "typical_p": 1,
        "epsilon_cutoff": 0,  # In units of 1e-4
        "eta_cutoff": 0,  # In units of 1e-4
        "tfs": 1,
        "top_a": 0,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "repetition_penalty_range": 0,
        "top_k": 40,
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "penalty_alpha": 0,
        "length_penalty": 1,
        "early_stopping": False,
        "mirostat_mode": 0,
        "mirostat_tau": 5,
        "mirostat_eta": 0.1,
        "grammar_string": "",
        "guidance_scale": 1,
        "negative_prompt": "",
        "seed": -1,
        "add_bos_token": True,
        "truncation_length": 2048,
        "ban_eos_token": False,
        "custom_token_bans": "",
        "skip_special_tokens": True,
        "stopping_strings": [],
    }

    response = requests.post(URI, json=request)

    if response.status_code == 200:
        result = response.json()["results"][0]["text"].split("\n")
        if len(result) == len(line):
            return True
    return False


def iter_book(book: List[str]):
    limit = 500
    seg = []
    count = 0
    for line in book:
        if count + len(line) > limit:
            yield seg, count
            seg = [line]
            count = len(line)
        else:
            seg.append(line)
            count += len(line)


if __name__ == "__main__":
    with open("book.txt") as f:
        book = [line.replace("　", " ").strip() for line in f.readlines()]
        book = [line for line in book if len(line) > 0]

    ts_start = time.time()
    test_time_limit = 2 * 60

    count_total = 0
    count_success = 0
    count_seg_total = 0
    count_seg_success = 0

    for seg, count in iter_book(book):
        is_success = translate(seg)
        count_total += count
        count_seg_total += 1
        if is_success:
            count_success += count
            count_seg_success += 1

        test_time = time.time() - ts_start
        print(f"{test_time:.2f} {is_success} {count}")
        if test_time > test_time_limit:
            print("")
            print(f"{CARD} {HOST}")
            print(f"Time: {test_time:.2f}s")
            print(f"Char: {count_success}/{count_total}")
            print(f"Seg:  {count_seg_success}/{count_seg_total}")
            speed_success = count_success / test_time
            speed_total = count_total / test_time
            print(f"CharSpeed:  {speed_success:.2f}/{speed_total:.2f}")
            break
