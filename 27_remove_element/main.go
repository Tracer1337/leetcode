package main

import "fmt"

func main() {
	got := solve([]int{3, 2, 2, 3}, 3)
	if got != 2 {
		fmt.Printf("[3,2,2,3]; got %d; want 2\n", got)
	}
	got = solve([]int{0, 1, 2, 2, 3, 0, 4, 2}, 2)
	if got != 5 {
		fmt.Printf("[0,1,2,2,3,0,4,2]; got %d; want 5\n", got)
	}
}

func solve(nums []int, val int) int {
	open := make([]int, 0)
	openIndex := 0
	k := 0
	for i, n := range nums {
		if n == val {
			open = append(open, i)
			continue
		}
		if len(open) > 0 {
			nums[open[openIndex]] = n
			openIndex++
			open = append(open, i)
		}
		k++
	}
	return k
}
