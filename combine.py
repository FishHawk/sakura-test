def read_file(filename):
    with open(filename) as f:
        return f.read().splitlines()


def cb(zh, zh9, target):
    print(f"{zh} + {zh9} => {target}")
    lines_zh = read_file(zh)
    lines_zh9 = [l for l in read_file(zh9) if l]

    lines_target = []
    count = 0
    for lines in lines_zh:
        if lines:
            lines_target.append(lines)
            count += 1
            if count % 3 == 0:
                lines_target.append(lines_zh9.pop(0))
        else:
            lines_target.append("")

    with open(target, "w") as f:
        f.write("jp\nsakura-0.8\nsakura-0.9\nsakura-0.9.1\n\n")
        f.write("\n".join(lines_target))


for i in range(1, 5):
    cb(
        f"tb{i}.translation.txt",
        f"zh.Ys.tb{i}.txt",
        f"tb{i}.translation.txt",
    )
