package main

import (
	"fmt"
)

func main() {
	got := solve([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4})
	want := 6
	if got != want {
		fmt.Printf("[-2,1,-3,4,-1,2,1,-5,4]; got %d; want %d\n", got, want)
	}
	got = solve([]int{1})
	want = 1
	if got != want {
		fmt.Printf("[1]; got %d; want %d\n", got, want)
	}
	got = solve([]int{5, 4, -1, 7, 8})
	want = 23
	if got != want {
		fmt.Printf("[5,4,-1,7,8]; got %d; want %d\n", got, want)
	}
	got = solve([]int{-1})
	want = -1
	if got != want {
		fmt.Printf("[-1]; got %d; want %d\n", got, want)
	}
}

func solve(nums []int) int {
	currSub := nums[0]
	maxSub := nums[0]
	for _, n := range nums[1:] {
		currSub = max(n, currSub+n)
		maxSub = max(currSub, maxSub)
	}
	return maxSub
}

func max(a int, b int) int {
	if a >= b {
		return a
	}
	return b
}
