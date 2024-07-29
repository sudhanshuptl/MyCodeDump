package main

// https://leetcode.com/problems/longest-common-prefix/description/
func longestCommonPrefix(strs []string) string {
	var cp string = strs[0]
	var l, wl int
	for _, word := range strs {
		l = len(cp)
		wl = len(word)

		if l > wl {
			l = wl
			cp = cp[:l]
		}
		for i := 0; i < l; i++ {
			if cp[i] != word[i] {
				cp = word[:i]
				break
			}
		}

	}
	return cp
}

// func main() {
// 	var strs = []string{"flower", "flow", "flight"}
// 	fmt.Println("---->", longestCommonPrefix(strs))
// }
