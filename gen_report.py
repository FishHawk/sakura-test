import re

import requests

pattern = re.compile("\\[\\[([AB<>=]+)\\]\\]")


def get_score(judgment):
    matches = pattern.findall(judgment)
    matches = [m for m in matches if m != ""]
    if len(set(matches)) == 0:
        return None, True
    elif len(set(matches)) == 1:
        return matches[0].strip("\n"), False
    else:
        return None, False


def judgment(question, answer, baseline):
    output = {"score": set()}
    for game in range(2):
        if game % 2 == 1:
            temp = baseline
            baseline = answer
            answer = temp
        judgment = ""
        url = "http://localhost/v1/workflows/run"
        headers = {"Authorization": "Bearer app-WbvxyZIRTqs4HLdO5gMXVben"}
        payload = {
            "inputs": {
                "question": question,
                "answer_1": baseline,
                "answer_2": answer,
            },
            "response_mode": "blocking",
            "user": "sakura",
        }
        r = requests.post(url, headers=headers, json=payload)
        print(r.text)
        new_judgment = r.json()["data"]["outputs"]["judgment"]
        judgment += "\n" + new_judgment
        score, try_again = get_score(judgment)

        while try_again:
            headers = {"Authorization": "Bearer app-jboODhEGzNv3NRYqDkAdUF9A"}
            payload["inputs"]["new_judgment"] = new_judgment
            r = requests.post(url, headers=headers, json=payload)
            new_judgment = r.json()["data"]["outputs"]["judgment"]
            judgment += "\n" + new_judgment
            score, try_again = get_score(judgment)

        output["score"].add(score)
        if "judgment" not in output:
            output["judgment"] = judgment

    return output


if __name__ == "__main__":
    for i in range(1, 5):
        report = []
        with open(f"tb{i}.translation.txt", "r") as f:
            count = 0
            for line in f.read().splitlines():
                if line:
                    count += 1
                    if count % 4 == 0:
                        answer = line
                        score = judgment(question, answer, baseline_answer)
                        print(score["score"])
                        if ("A>B" in score["score"] or "A>>B" in score["score"]) and (
                            "B>A" in score["score"] or "B>>A" in score["score"]
                        ):
                            report.append(
                                (question, baseline_answer, answer, score["judgment"])
                            )
                    elif count % 4 == 1:
                        question = line
                    elif count % 4 == 3:
                        baseline_answer = line
        with open(f"tb{i}.report.md", "w") as f:
            f.write(f"# TB{i}\n\n")
            for j, r in enumerate(report):
                f.write(f"### P{j + 1}\n\n")
                f.write(f"{r[0]}\n\n")
                f.write(f"{r[1]}\n\n")
                f.write(f"{r[2]}\n\n")
                f.write(f"{r[3]}\n\n")
