package main

import "fmt"

func main() {
	got := solve("hello", "ll")
	if got != 2 {
		fmt.Printf("'hello'; got %d; want 2\n", got)
	}
	got = solve("aaaa", "bba")
	if got != -1 {
		fmt.Printf("'aaaa'; got %d; want -1\n", got)
	}
	got = solve("", "")
	if got != 0 {
		fmt.Printf("''; got %d, want 0\n", got)
	}
	got = solve("a", "a")
	if got != 0 {
		fmt.Printf("'a'; got %d; want 0", got)
	}
}

func solve(haystack string, needle string) int {
	if needle == "" {
		return 0
	}
	if len(haystack) < len(needle) {
		return -1
	}
	for i := 0; i <= len(haystack)-len(needle); i++ {
		if haystack[i:i+len(needle)] == needle {
			return i
		}
	}
	return -1
}
