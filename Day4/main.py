# Had to look this one up, kept running into bug, not enough time 
def part1(grid):
  count = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] != "X":
        continue
      for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
          if dr == dc == 0:
            continue
          if not (0 <= r + 3 * dr < len(grid) and 0 <= c + 3 * dc <len(grid[0])):
            continue
          if grid[r + dr][c+dc] == "M" and grid[r+2*dr][c+2*dc] == "A" and grid[r+3*dr][c+3*dc] == "S":
            count +=1
  return count

def part2(grid):
  count = 0
  for r in range(len(grid) -1) :
    for c in range(len(grid[0]) - 1):
      if grid[r][c] != "A":
        continue
      corners = [grid[r - 1][c - 1], grid[r-1][c+1], grid[r+1][c+1], grid[r+1][c-1]]
      if corners == ["M", "M", "S", "S"]:
        count += 1 
      elif corners == ["M", "S", "S", "M"]:
        count += 1
      elif corners == ["S", "S", "M", "M"]:
        count += 1
      elif corners == ["S", "M", "M", "S"]:
        count += 1
  return count

def main():
  puzzle = open("input.txt", "r").read().splitlines()
  print(puzzle)
  part_1_result = part1(puzzle)
  print(f"Part 1: {part_1_result}")
  part_2_result = part2(puzzle)
  print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
  main()