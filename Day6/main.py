from time import perf_counter_ns

def turn_right(direction):
    match direction:
      case (-1,0):
        direction = [0,1]
      case (1,0):
        direction = [0,-1]
      case (0,-1):
        direction = [-1,0]
      case (0,1):
        direction = [1,0]
    return direction



def part1(puzzle, direction, start):
  positions = set()
  while True:
    try:
      x, y = direction
      r, c = start
      place = puzzle[r+x][c+y]
      # print(x,y)
      if place != "#":
        positions.add((r+x, c+y))
        if r+x < 0 or c+y < 0:
          break
        start = [r+x, c+y]
      elif place == "#":
        direction = turn_right(direction)
    except IndexError:
      break
  return positions

def main():
  puzzle = open("example.txt", "r").read().splitlines()
  for r_index, row in enumerate(puzzle):
    for c_index, col in enumerate(row):
      if col in ["<",">", "v", "^"]:
        start = [r_index, c_index]
        if col == "<":
          direction = (0, -1)
        elif col == ">":
          direction = ( 0, 1)
        elif col == "^":
          direction = (-1, 0)
        elif col == "v":
          direction = (1, 0)
  start_time = perf_counter_ns()
  positions = part1(puzzle, direction, start)
  print(f"Part 1: {len(positions)}")
  # part_2 = part2(puzzle)
  # print(f"Part 2: {part_2}")
  print(f"TTC: {perf_counter_ns() - start_time}ns")
      


        


if __name__ == "__main__":
  main()