def readFile(file_name: str):
    with open(file_name, "r") as f:
        data = f.read()
    return data


def check_structure(data: list[int]):
    diff = [a - b for a, b in zip(data, data[1:])]
    is_increasing_or_decreasing = all(i > 0 for i in diff) or all(i < 0 for i in diff)
    is_inbounds = all(0 < abs(i) <= 3 for i in diff)
    if is_increasing_or_decreasing and is_inbounds:
        return True
    else:
        return False


def check_structure_with_error(data: list[int]):
    # Fails
    diff = [a - b for a, b in zip(data, data[1:])]
    is_increasing_or_decreasing = all(i > 0 for i in diff) or all(i < 0 for i in diff)
    errors = 0
    if not is_increasing_or_decreasing:
        # Check each one for single issue
        greater_than_error = 0
        for x in diff:
            if x > 0:
                greater_than_error += 1
        less_than_error = 0
        for x in diff:
            if x < 0:
                less_than_error += 1
        if greater_than_error == 1 or less_than_error == 0:
            errors += 1
            is_increasing_or_decreasing = True
        elif greater_than_error == 0 or less_than_error == 1:
            errors += 1
            is_increasing_or_decreasing = True
        else:
            errors += greater_than_error + less_than_error

    is_inbounds = all(0 < abs(i) <= 3 for i in diff)
    if not is_inbounds and errors == 0:
        for x in diff:
            if not 0 < abs(x) <= 3:
                errors += 1
    if is_increasing_or_decreasing and is_inbounds or errors == 1:
        return True
    else:
        return False


def part1(info: list[list[int]]):
    result = 0
    for line in info:
        valid = check_structure(line)
        if valid:
            result += 1

    return result


def part2(info: list[list[int]]):
    result = 0
    for line in info:
        valid = check_structure(line)
        if valid:
            result += 1
        else:
            for i in range(len(line)):
                levels = line[:i] + line[i + 1 :]
                valid = check_structure(levels)
                if valid:
                    result += 1
                    break

    return result


def main():
    info = readFile("input.txt")
    data = []

    for line in info.splitlines():
        info = list(int(x) for x in line.split())
        data.append(info)
    part_1 = part1(data)
    print(f"Part 1: {part_1}")
    part_2 = part2(data)
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()
