def part1(antenna):
  antinode = set()
  for array in antenna.values():
    for i in range(len(array)):
      for c in range(len(array)):
        if i == c:
          continue
        r1, c1 = array[i]
        r2, c2 = array[c]
        antinode.add((2*r1-r2, 2*c1-c2))
        antinode.add((2*r2-r1, 2*c2-c1))
  return antinode

def part2(antenna, row_len, col_len):
  antinode = set()
  for array in antenna.values():
    for i in range(len(array)):
      for c in range(len(array)):
        if i == c:
          continue
        r1, c1 = array[i]
        r2, c2 = array[c]
        antinode.add((r1,c1))
        antinode.add((r2,c2))
        r_diff = r1 - r2
        c_diff = c1 - c2
        r_new = 2 * r1 - r2
        c_new = 2 * c1 - c2
        while 0 <= r_new < row_len and 0<= c_new < col_len:
            antinode.add((r_new,c_new))
            r_new += r_diff
            c_new += c_diff
        r_diff = r2 - r1
        c_diff = c2 - c1
        r_new = 2 * r2 - r1
        c_new = 2 *  c2 - c1
        while 0 <= r_new < row_len and 0<= c_new < col_len:
            antinode.add((r_new,c_new))
            r_new += r_diff
            c_new += c_diff

  for n in antinode:
    print(n)
  return antinode

def main():
  grid = open("input.txt", "r").read().splitlines()
  antenna = {}
  for r, row in enumerate(grid):
    for c, col in enumerate(row):
      if col != ".":
        if antenna.get(col):
          antenna[str(col)].append((r,c))
        else:
          antenna[str(col)] = []
          antenna[str(col)].append((r,c))
  row = len(grid)
  col = len(grid[0])
  counter = 0
  antinode = part1(antenna)
  for node in antinode:
    r, c = node
    if 0 <= r < row and 0 <= c < col:
      counter += 1
  print(f"Part 1 : {counter}")
  puzzle = []
  for line in grid:
    puzzle.append([x for x in line])
  part_2 = part2(antenna, row, col)
  for x,y in part_2:
    puzzle[x][y] = "#"

  for p in puzzle:
    print(p)

  print(f"Part 2 : {len(part_2)}")



if __name__ == "__main__":
  main()