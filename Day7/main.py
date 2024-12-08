
def possible_values(array):
  if len(array) == 1:
    return {array[0]}
  subset = possible_values(array[:-1])
  return {x + array[-1] for x in subset} | {x * array[-1] for x in subset} | {int(str(x) + str(array[-1])) for x in subset}


def main():
  total = 0
  data = open("example.txt", "r").read().splitlines()
  for line in data:
    left, right = line.split(": ")
    target = int(left)
    array = [int(x) for x in right.split()]
    if target in possible_values(array):
      total += target
  print(f"Part 1: {total}")


if __name__ == "__main__":
  main()