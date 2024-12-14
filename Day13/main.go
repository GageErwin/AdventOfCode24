package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

// Button A: X+94, Y+34
// Button B: X+22, Y+67
// Prize: X=8400, Y=5400

func part1(targets []int) (int, int) {
	ax, ay, bx, by, px, py := targets[0], targets[1], targets[2], targets[3], targets[4], targets[5]
	d := ax*by - bx*ay
	d1 := px*by - py*bx
	d2 := py*ax - px*ay

	if d1%d != 0 || d2%d != 0 {
		return 0, 0
	}

	return d1 / d, d2 / d
}

func part2(targets []int) (int, int) {
	ax, ay, bx, by, px, py := targets[0], targets[1], targets[2], targets[3], targets[4], targets[5]
	px += 10000000000000
	py += 10000000000000
	d := ax*by - bx*ay
	d1 := px*by - py*bx
	d2 := py*ax - px*ay

	if d1%d != 0 || d2%d != 0 {
		return 0, 0
	}

	return d1 / d, d2 / d
}

func main() {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	dataSlice := strings.Split(string(data), "\n\n")
	var targetSlice [][]int
	for _, line := range dataSlice {
		var targets []int
		digits := regexp.MustCompile(`\d+`)
		buttons := digits.FindAllString(line, -1)
		for _, but := range buttons {
			buttonValue, err := strconv.Atoi(but)
			if err != nil {
				panic(err)
			}
			targets = append(targets, buttonValue)
		}
		targetSlice = append(targetSlice, targets)
	}
	resultA := 0
	resultB := 0
	for _, values := range targetSlice {
		a, b := part1(values)
		resultA += a * 3
		resultA += b
		c, d := part2(values)
		resultB += c * 3
		resultB += d
	}
	fmt.Println("Part 1: ", resultA)
	fmt.Println("Part 2: ", resultB)
}
