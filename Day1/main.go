package main

// TODO: Fails

import (
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
	"time"
)

// var inputFile = "example.txt"

var inputFile = "input.txt"

func readFile(filePath string) (string, error) {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func stringArrToint(data []string) ([]int, error) {
	var intArray []int
	for _, value := range data {
		if value == "" {
			continue
		}
		value = strings.ReplaceAll(value, "\r", "")
		inter, err := strconv.Atoi(value)
		if err != nil {
			log.Fatal(err)
		}
		intArray = append(intArray, inter)
	}
	return intArray, nil
}

func part1(data1 []int, data2 []int) int {
	var totalDiff int
	for i := range data1 {
		value1 := data1[i]
		value2 := data2[i]
		var diff int
		if value1 >= value2 {
			diff = value1 - value2
		} else {
			diff = value2 - value1
		}
		totalDiff += diff
	}
	return totalDiff
}

func part2(data1 []int, data2 []int) int {
	var total int
	for _, value := range data1 {
		var count int
		for _, find := range data2 {
			if value == find {
				count++
			}
		}
		timesFound := value * count
		total += timesFound
	}

	return total
}

func main() {
	start := time.Now()
	data, err := readFile(inputFile)
	if err != nil {
		log.Fatal(err)
	}
	dataArr := strings.Split(data, "\n")
	var array1 []string
	var array2 []string
	for _, numb := range dataArr {
		numbSplit := strings.Split(numb, " ")
		array1 = append(array1, numbSplit[0])
		lastIndex := len(numbSplit)
		array2 = append(array2, numbSplit[lastIndex-1])
	}
	ayy1, err := stringArrToint(array1)
	if err != nil {
		log.Fatal(err)
	}
	ayy2, err := stringArrToint(array2)
	if err != nil {
		log.Fatal(err)
	}
	slices.Sort(ayy1)
	slices.Sort(ayy2)
	// Part 1
	part1Time := time.Now()
	totalDiff := part1(ayy1, ayy2)
	fmt.Println("Part 1: ", totalDiff)
	fmt.Printf("TTC: %d ns\n\n", time.Since(part1Time).Nanoseconds())
	// Part 2
	part2Time := time.Now()
	oftenMul := part2(ayy1, ayy2)
	fmt.Println("Part 2: ", oftenMul)
	fmt.Printf("TTC: %d ns\n", time.Since(part2Time).Nanoseconds())
	fmt.Printf("Total Time: %d ns", time.Since(start).Nanoseconds())
}
