package main

import (
	"fmt"
	"os"
)

var values = map[rune]int{
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000,
}

var multiple = map[string]int{
	"IV": 4,
	"IX": 9,
	"XL": 40,
	"XC": 90,
	"CD": 400,
	"CM": 900,
}

func romanToInt(s string) int {
	result := 0
	i := 0
	for i < len(s) {
		c := s[i]
		if i < len(s)-1 {
			next := s[i+1]
			str := string(c) + string(next)
			if value, ok := multiple[str]; ok {
				result += value
				i += 2
				continue
			}
		}
		result += values[rune(c)]
		i++
	}
	return result
}

func main() {
	if len(os.Args) == 1 {
		panic("Missing argument")
	}
	fmt.Println(romanToInt(os.Args[1]))
}
