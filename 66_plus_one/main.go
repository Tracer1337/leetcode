package main

import (
	"fmt"
)

func test(arg0 []int, want []int) {
	isValid := func(got []int) bool {
		if len(got) != len(want) {
			return false
		}
		for i := range got {
			if got[i] != want[i] {
				return false
			}
		}
		return true
	}
	got := solve(arg0)
	if !isValid(got) {
		fmt.Printf("%d; got %d; want %d\n", arg0, got, want)
	}
}

func main() {
	test([]int{1, 2, 3}, []int{1, 2, 4})
	test([]int{4, 3, 2, 1}, []int{4, 3, 2, 2})
	test([]int{9}, []int{1, 0})
	test([]int{9, 9}, []int{1, 0, 0})
	test([]int{8, 9, 9, 9}, []int{9, 0, 0, 0})
}

func solve(digits []int) []int {
	digits[len(digits)-1]++
	carry := 0
	for i := len(digits) - 1; i >= 0; i-- {
		digits[i] += carry
		carry = 0
		if digits[i] >= 10 {
			carry = digits[i] - 9
			digits[i] = 0
		}
	}
	if carry > 0 {
		digits = append([]int{carry}, digits...)
	}
	return digits
}
