import re


def readFile(file_name: str):
    with open(file_name, "r") as f:
        data = f.read()
    return data


def part1(info: str):
    pattern = r"mul\(\d+,\d+\)"
    match = re.compile(pattern)
    matches: list[str] = match.findall(info)
    result = 0
    for m in matches:
        x, y = m.replace("mul(", "").replace(")", "").split(",")
        result += int(x) * int(y)
    return result


def part2(info: str):
    dos = info.split("don't()")
    valid = dos[0]
    for line in dos:
        try:
            do_index = line.index("do()")
            valid += line[do_index::]
        except ValueError:
            continue
    pattern = r"mul\(\d+,\d+\)"
    match = re.compile(pattern)
    matches: list[str] = match.findall(valid)
    result = 0
    for m in matches:
        x, y = m.replace("mul(", "").replace(")", "").split(",")
        result += int(x) * int(y)
    return result


def main():
    info = readFile("input.txt")
    part_1_result = part1(info)
    print(f"Part 1: {part_1_result}")
    part_2_result = part2(info)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()
    # 344715
    # 50745884
