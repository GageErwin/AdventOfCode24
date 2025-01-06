import time


def readFile(file_name: str):
    with open(file_name, "r") as f:
        data = f.read()
    return data


def part1(data1, data2):
    total_diff = 0
    for i, _ in enumerate(data1):
        value1 = data1[i]
        value2 = data2[i]
        if value1 >= value2:
            total_diff += value1 - value2
        else:
            total_diff += value2 - value1

    return total_diff


def part2(data1, data2):
    total_diff = 0
    for i, _ in enumerate(data1):
        value1 = data1[i]
        total_diff += value1 * data2.count(value1)

    return total_diff


def main():
    start_time = time.perf_counter_ns()
    data = readFile("example.txt")
    # data = readFile("input.txt")
    data_list = data.splitlines()
    list1 = []
    list2 = []
    for d in data_list:
        values = d.split()
        list1.append(int(values[0]))
        value2 = values[-1].replace("\r", "")
        list2.append(int(value2))

    list1.sort()
    list2.sort()
    part1_time = time.perf_counter_ns()
    part1_value = part1(list1, list2)
    print(f"Part 1: {part1_value}")
    print(f"TTC: {time.perf_counter_ns() - part1_time}ns\n")
    part2_time = time.perf_counter_ns()
    part2_value = part2(list1, list2)
    print(f"Part 2: {part2_value}")
    print(f"TTC: {time.perf_counter_ns() - part2_time}ns")
    print(f"Total Time: {time.perf_counter_ns() - start_time}")


if __name__ == "__main__":
    main()
