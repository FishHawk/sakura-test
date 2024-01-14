def read_file(filename):
    with open(filename) as f:
        return f.read().splitlines()


def cb(jp, zh8, zh9, target):
    print(f"{jp} + {zh8} + {zh9} => {target}")
    lines_jp = read_file(jp)
    lines_zh8 = read_file(zh8)
    lines_zh9 = read_file(zh9)

    lines_target = []
    for lines in zip(lines_jp, lines_zh8, lines_zh9):
        if lines[0]:
            lines_target += lines
        else:
            lines_target.append("")

    with open(target, "w") as f:
        f.write("jp\nsakura-0.8\nsakura-0.9\n\n")
        f.write("\n".join(lines_target))


for i in range(1, 6):
    cb(
        f"tb{i}.txt",
        f"zh.Ys.tb{i}.txt",
        f"zh.Ys.tb9-{i}.txt",
        f"tb{i}.translation.txt",
    )
