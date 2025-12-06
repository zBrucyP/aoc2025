package main

import (
	"bufio"
	"os"
	"fmt"
	"strings"
	"strconv"
	"sort"
	"time"
)

func is_ingredient_fresh(ranges [][]int, ingredient int) bool {
	for _, r := range ranges {
		if ingredient >= r[0] && ingredient <= r[1] {
			return true
		}
	}

	return false
}

func number_of_fresh_ingredients_in_range(singleRange []int) int {
	return singleRange[1] - singleRange[0] + 1
}

func combine_ranges(ranges [][]int) [][]int {
	if len(ranges) == 0 {
		return ranges
	}
	// sort ranges by start value
	sorted := make([][]int, len(ranges))
	copy(sorted, ranges)
	sort.Slice(sorted, func(i, j int) bool {
		return sorted[i][0] < sorted[j][0]
	})
	combinedRanges := [][]int{}
	for _, r := range sorted {
		// start somewhere
		if len(combinedRanges) == 0 {
			combinedRanges = append(combinedRanges, r)
			continue
		}
		lastRange := combinedRanges[len(combinedRanges)-1]
		// last in combined: [0, 2]
		// range:            [1, 3] 
		if r[0] <= lastRange[1] {
			if r[1] > lastRange[1] {
				// only do it if the new range goes further. Caused failure before
				// ex: 
				// last:  [0, 4]
				// range: [1, 3]
				lastRange[1] = r[1]
			}
		} else {
			combinedRanges = append(combinedRanges, r)
		}
	}

	return combinedRanges
}

func main() {
	start := time.Now()
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	// process input
	ranges := [][]int{}
	ingredients := []int{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if strings.Contains(line, "-") {
			parts := strings.Split(line, "-")
			start, startErr := strconv.Atoi(parts[0])
			end, endErr := strconv.Atoi(parts[1])
			if startErr != nil || endErr != nil {
				panic("Invalid number in range")
			}
			ranges = append(ranges, []int{start, end})
		} else if strings.TrimSpace(line) == "" {
			continue
		} else {
			ingredientId, err := strconv.Atoi(line)
			if err != nil {
				panic("Invalid ingredient ID")
			}
			ingredients = append(ingredients, ingredientId)
		}
	}

	// part 1
	// total_fresh_ingredients := 0
	// for _, ingredient := range ingredients {
	// 	if is_ingredient_fresh(ranges, ingredient) {
	// 		total_fresh_ingredients++
	// 	}
	// }

	// part 2
	total_fresh_ingredients := 0
	combinedRanges := combine_ranges(ranges)
	for _, r := range combinedRanges {
		total_fresh_ingredients += number_of_fresh_ingredients_in_range(r)
	}
	
	fmt.Println("Total fresh ingredients:", total_fresh_ingredients)

	elapsed := time.Since(start)
	fmt.Printf("Execution time: %f microseconds\n", float64(elapsed.Microseconds()))
}


// 332990462542649 your answer is too low