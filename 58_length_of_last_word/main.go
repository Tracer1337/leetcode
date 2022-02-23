package main

import (
	"fmt"
	"strings"
)

func test(arg0 string, want int) {
	got := solve(arg0)
	if got != want {
		fmt.Printf("'%s'; got %d; want %d\n", arg0, got, want)
	}
}

func main() {
	test("Hello World", 5)
	test("   fly me   to   the moon  ", 4)
	test("luffy is still joyboy", 6)
}

func solve(s string) int {
	s = strings.TrimSpace(s)
	l := 0
	for i := len(s) - 1; i >= 0; i-- {
		c := rune(s[i])
		if c == ' ' {
			break
		}
		l++
	}
	return l
}
