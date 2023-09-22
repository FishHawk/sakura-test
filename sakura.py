from typing import List
import requests

endpoint = "http://192.168.1.162:8000"


def translate_line(
    s: str,
    frequency_penalty: int | None = None,
    top_p: int | None = None,
):
    res = requests.post(
        endpoint + "/v1/chat/completions",
        headers={"Content-Type": "application/json"},
        json={
            "model": "Sakura-13B-Galgame",
            "messages": [
                {
                    "role": "user",
                    "content": f"将下面的日文文本翻译成中文：{s}",
                }
            ],
            "frequency_penalty": frequency_penalty,
            "top_p": top_p,
            "max_tokens": 512,
        },
    )
    return res.json()


def translate_line_p(s: str):
    return translate_line(s, frequency_penalty=1, top_p=0)


def translate_lines(
    lines: List[str],
    frequency_penalty: int | None = None,
    top_p: int | None = None,
):
    result = []
    for index, s in enumerate(lines):
        print(f"{index}/{len(lines)}")
        obj = translate_line(
            s,
            frequency_penalty=frequency_penalty,
            top_p=top_p,
        )
        content = obj["choices"][0]["message"]["content"]
        result.append(content)
    return result


def translate_lines_p(lines: List[str]):
    return translate_lines(lines, frequency_penalty=1, top_p=0)
