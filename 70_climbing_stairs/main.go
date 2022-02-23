package main

import (
	"fmt"
)

func test(arg0 int, want int) {
	got := solve(arg0)
	if got != want {
		fmt.Printf("%d; got %d; want %d\n", arg0, got, want)
	}
}

func main() {
	test(1, 1)
	test(2, 2)
	test(3, 3)
}

func solve(n int) int {
	memo := map[int]int{1: 1, 2: 2}
	var climb func(n int) int
	climb = func(n int) int {
		if v, ok := memo[n]; ok {
			return v
		}
		memo[n] = climb(n-1) + climb(n-2)
		return memo[n]
	}
	return climb(n)
}
