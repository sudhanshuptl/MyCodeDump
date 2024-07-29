package main

//https://leetcode.com/problems/roman-to-integer/description/

var romanMap = map[byte]int{
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000,
}

func romanToInt(s string) int {
	var result int
	n := len(s)

	for i := 0; i < n; i++ {
		value := romanMap[s[i]]

		// Check if this is a subtractive combination
		if i < n-1 && value < romanMap[s[i+1]] {
			result -= value
		} else {
			result += value
		}
	}

	return result
}

// func main() {
// 	// Example 1
// 	roman1 := "III"
// 	fmt.Printf("Roman numeral: %s, Integer: %d\n", roman1, romanToInt(roman1)) // Output: 3

// 	// Example 2
// 	roman2 := "LVIII"
// 	fmt.Printf("Roman numeral: %s, Integer: %d\n", roman2, romanToInt(roman2)) // Output: 58

// 	// Example 3
// 	roman3 := "MCMXCIV"
// 	fmt.Printf("Roman numeral: %s, Integer: %d\n", roman3, romanToInt(roman3)) // Output: 1994
// }
