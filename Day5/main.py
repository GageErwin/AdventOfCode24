from time import perf_counter_ns
from copy import copy


def part1(rules, checks):
    result = 0
    for line in checks:
        nums = [int(x) for x in line.split(",")]
        valid = True
        for before, after in rules:
            if before in nums or after in nums:
                try:
                    before_index = nums.index(before)
                except Exception:
                    before_index = None
                try:
                    after_index = nums.index(after)
                except Exception:
                    after_index = None
                if before_index is not None and after_index is not None:
                    if before_index > after_index:
                        valid = False
        if valid:
            result += nums[int(len(nums) / 2)]
    return result


def part2(rules, checks):
    result = 0
    for line in checks:
        nums = [int(x) for x in line.split(",")]
        corrected = False
        while True:
            for before, after in rules:
                if before in nums or after in nums:
                    try:
                        before_index = nums.index(before)
                    except Exception:
                        before_index = None
                    try:
                        after_index = nums.index(after)
                    except Exception:
                        after_index = None
                    if before_index is not None and after_index is not None:
                        if before_index > after_index:
                            before_num = copy(nums[before_index])
                            after_num = copy(nums[after_index])
                            nums[before_index] = after_num
                            nums[after_index] = before_num
                            corrected = True
                            break
            else:
                break
        if corrected:
            result += nums[int(len(nums) / 2)]
    return result


def main():
    data = open("example.txt", "r").read().splitlines()
    rules = []
    checks = []
    for line in data:
        if "|" in line:
            x, y = line.split("|")
            rules.append((int(x), int(y)))
        elif "," in line:
            checks.append(line)
    print(rules)
    print(checks)
    start_time = perf_counter_ns()
    part_1_solution = part1(rules, checks)
    print(f"Part 1: {part_1_solution}")
    part_2_solution = part2(rules, checks)
    print(f"TTC part 1: {perf_counter_ns() - start_time}ns")
    print(f"Part 2: {part_2_solution}")
    print(f"TTC: {perf_counter_ns() - start_time}ns")


if __name__ == "__main__":
    main()
