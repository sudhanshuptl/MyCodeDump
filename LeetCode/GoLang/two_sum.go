package main

import (
	"slices"
)

// https://leetcode.com/problems/two-sum/
func twoSum(nums []int, target int) []int {
	var cmap = make(map[int][]int, len(nums))
	var result []int

	//create  map to define current value and value needed to add up to the targe
	for i, val := range nums {
		if _, found := cmap[val]; found {
			cmap[val] = append(cmap[val], i)
		} else {
			cmap[val] = []int{i}
		}

	}

	// iterate through map and check if for each key
	for key, indexes := range cmap {
		remainingVal := target - key
		if key == remainingVal { //special case where same number add up to same number to meet target
			if len(indexes) > 1 {
				result = append(result, indexes[0])
				result = append(result, indexes[1])
				break
			}
		} else if index2, found := cmap[remainingVal]; found {
			result = append(result, indexes[0])
			result = append(result, index2[0])
			break
		}

	}
	slices.Sort(result)
	return result
}

// func main() {
// 	nums := []int{3, 2, 4}
// 	target := 6
// 	fmt.Println("result - ", twoSum(nums, target))
// }
