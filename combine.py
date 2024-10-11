def read_file(filename):
    with open(filename) as f:
        return f.read().splitlines()


def diff(diff_file, tb_files):
    tb_text_list = [read_file(f) for f in tb_files]
    text_output = list(tb_files)
    text_output.append("")

    for i in range(len(tb_text_list[0])):
        if not tb_text_list[0][i]:
            continue
        for t in tb_text_list:
            text_output.append(t[i])
        text_output.append("")

    with open(diff_file, "w") as f:
        f.write("\n".join(text_output))


def report(report_file, tb_files):
    tb_text_list = [read_file(f) for f in tb_files]
    text_output = [f"# {tb_files[0]}\n"] + [f"- {f}" for f in tb_files] + [""]

    count = 1
    for i in range(len(tb_text_list[0])):
        if not tb_text_list[0][i]:
            continue
        text_output.append(f"### P{count}\n")
        for t in tb_text_list:
            text_output.append(" " * 4 + t[i] + "\n")
        text_output.append("")
        count += 1

    with open(report_file, "w") as f:
        f.write("\n".join(text_output))


for i in range(1, 5):
    tb_files = [
        f"data/tb{i}.txt",
        f"data/zh.Ys.tb{i}.v0.9.2.txt",
        f"data/zh.Ys.tb{i}.v1.0.txt",
    ]
    diff(f"tb{i}.diff.v1.0.md", tb_files)
    report(f"tb{i}.report.v1.0.md", tb_files)
