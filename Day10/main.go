package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

var fileName = "example.txt"

// var fileName = "input.txt"

// func dedupItems(array [][]int) [][]int {
// 	var deduped [][]int
// outerloop:
// 	for _, item := range array {
// 		for _, value := range deduped {
// 			if item[0] == value[0] && item[1] == value[1] && item[2] == value[2] {
// 				continue outerloop
// 			}
// 		}
// 		deduped = append(deduped, item)
// 	}
// 	return deduped
// }

func readFile(filePath string) (string, error) {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func checkAround(grid [][]int, starts [][]int, count int) int {
	if len(starts) == 0 {
		fmt.Println(count)
		return count
	}
	// starts = dedupItems(starts)
	// fmt.Println("START: ", starts)
	// positions, starts = starts[0], starts[1:]
	positions := starts[len(starts)-1]
	starts = starts[:len(starts)-1]
	r := positions[0]
	c := positions[1]
	find := positions[2]
	if r-1 >= 0 && grid[r-1][c] == find {
		if find == 9 {
			count += 1
		} else {
			var s []int
			s = append(s, r-1, c, find+1)
			starts = append(starts, s)
		}
	}
	if r+1 < len(grid)-1 && grid[r+1][c] == find {
		if find == 9 {
			count += 1
		} else {

			var s []int
			s = append(s, r+1, c, find+1)
			starts = append(starts, s)
		}
	}
	if c-1 >= 0 && grid[r][c-1] == find {
		if find == 9 {
			count += 1
		} else {

			var s []int
			s = append(s, r, c-1, find+1)
			starts = append(starts, s)
		}
	}
	if c+1 < len(grid)-1 && grid[r][c+1] == find {
		if find == 9 {
			count += 1
		} else {
			var s []int
			s = append(s, r, c+1, find+1)
			starts = append(starts, s)
		}
	}
	// fmt.Println("END: ", starts)
	return checkAround(grid, starts, count)
}

func part1(grid [][]int) int {
	result := 0
	var starts [][]int
	for r, row := range grid {
		for c, col := range row {
			if col == 0 {
				var s []int
				s = append(s, r, c)
				starts = append(starts, s)
			}
		}
	}
	for _, values := range starts {
		var ss [][]int
		r := values[0]
		c := values[1]
		if r == 0 && c == 2 {
			fmt.Println(grid[r][c+1])
		}
		fmt.Println(r, c)
		find := 2
		if r-1 > 0 && grid[r-1][c] == 1 {
			var s []int
			s = append(s, r-1, c, find)
			ss = append(ss, s)
		}
		if r+1 < len(grid) && grid[r+1][c] == 1 {
			var s []int
			s = append(s, r+1, c, find)
			ss = append(ss, s)
			fmt.Println(r, c)
		}
		if c-1 > 0 && grid[r][c-1] == 1 {
			var s []int
			s = append(s, r, c-1, find)
			ss = append(ss, s)
		}
		if c+1 < len(grid) && grid[r][c+1] == 1 {
			var s []int
			s = append(s, r, c+1, find)
			ss = append(ss, s)
		}
		if len(ss) != 0 {
			fmt.Println(ss)
			check := checkAround(grid, ss, 0)
			if check != 0 {
				result += check
			}
		}
	}
	return result
}

func main() {
	data, err := readFile(fileName)
	if err != nil {
		panic(err)
	}
	var grid [][]int
	rows := strings.Split(data, "\n")
	for _, r := range rows {
		var row []int
		for _, c := range r {
			value := string(c)
			intValue, err := strconv.Atoi(value)
			if err != nil {
				panic(err)
			}
			row = append(row, intValue)
		}
		grid = append(grid, row)
	}
	startTime := time.Now()
	partOne := part1(grid)
	fmt.Println(partOne)
	duration := time.Since(startTime).Nanoseconds()
	fmt.Printf("TTC: %dns\n", duration)
}
