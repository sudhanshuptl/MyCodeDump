package main

import (
"fmt"
)
func Names() (first string, second string) {
	first = "Foo"
	second = "Bar"
	return
}
func main() {
	// Here I did not return or passed the arguments but results are filled in n1 and n2
	// very unique feature.
	n1, n2 := Names()
	fmt.Println(n1, n2)
}
