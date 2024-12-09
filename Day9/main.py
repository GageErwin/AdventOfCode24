from itertools import batched
from time import perf_counter_ns


def main():
    start = perf_counter_ns()
    data = open("input.txt", "r").read()
    file_format = ""
    for i, files in enumerate(batched(data, 2)):
        if len(files) == 2:
            block = int(files[0])
            free = int(files[1])
            file_format += f"{i}" * block
            file_format += "." * free
        elif len(files) == 1:
            block = int(files[0])
            file_format += f"{i}" * block
    file_format_split = [x for x in file_format]
    num_count = 0
    for value in file_format_split:
        if value.isdigit():
            num_count += 1
    for index, x in enumerate(file_format_split[::-1]):
        if x == ".":
            continue
        for i, char in enumerate(file_format_split):
            if char == ".":
                file_format_split[i] = x
                break

    for i in range(num_count, len(file_format_split)):
        file_format_split[i] = "."
    result = 0
    for i, num in enumerate(file_format_split):
        if num.isdigit():
            result += i * int(num)
    print(f"Part 1: {result}")
    print(f"TTC: {perf_counter_ns() - start}ns")


if __name__ == "__main__":
    main()
