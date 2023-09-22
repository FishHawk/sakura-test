from sakura import *


def read_file(filename):
    with open(filename, "r") as f:
        return f.readlines()


def write_file(filename, lines):
    with open(filename, "w") as f:
        f.write("\n".join(lines) + "\n")


def translate_file_with_parameters():
    jp = read_file("text.jp")
    gpt = read_file("text.gpt")
    sa = translate_lines_p(jp)
    write_file("text.sa", sa)

    packed = ["日文", "GPT", "Sakura", ""]
    for lines in zip(jp, gpt, sa):
        for s in lines:
            packed.append(s.strip())
        packed.append("")
    write_file("text.sa-packed", packed)


if __name__ == "__main__":
    translate_file_with_parameters()
