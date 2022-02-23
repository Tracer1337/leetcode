package main

import (
	"fmt"
)

func main() {
	got := solve([]int{1, 3, 5, 6}, 5)
	if got != 2 {
		fmt.Printf("'hello'; got %d; want 2\n", got)
	}
	got = solve([]int{1, 3, 5, 6}, 2)
	if got != 1 {
		fmt.Printf("'hello'; got %d; want 1\n", got)
	}
	got = solve([]int{1, 3, 5, 6}, 7)
	if got != 4 {
		fmt.Printf("'hello'; got %d; want 4\n", got)
	}
	got = solve([]int{1, 3, 5, 6}, 0)
	if got != 0 {
		fmt.Printf("'hello'; got %d; want 0\n", got)
	}
}

func solve(nums []int, target int) int {
	min := 0
	max := len(nums) - 1
	mid := 0
	for min <= max {
		mid = (min + max) / 2
		if nums[mid] < target {
			min = mid + 1
		} else if nums[mid] > target {
			max = mid - 1
		} else {
			return mid
		}
	}
	if nums[mid] > target {
		return mid
	}
	return mid + 1
}
