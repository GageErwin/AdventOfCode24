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
    file_format = [x for x in file_format]
    back_count = len(file_format) - 1
    while back_count >= 0:
        last = file_format[back_count]
        if last != ".":
            for i, num in enumerate(file_format):
                if num == ".":
                    file_format[i] = last
                    file_format[back_count] = "."
                    break
        else:
            back_count -= 1

    file_format.pop(0)
    file_format.append(".")
    print(file_format)
    result = 0
    for i, num in enumerate(file_format):
        if num != ".":
            result += i * int(num)
    print(f"Part 1: {result}")
    print(f"TTC: {perf_counter_ns() - start}ns")


if __name__ == "__main__":
    main()
