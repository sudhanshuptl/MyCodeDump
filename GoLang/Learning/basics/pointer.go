package main

import "fmt"

func main() {
	//// different way than c to create pointer as it will return pointer to an integer
	// new function create variable and return pointer to it
	p := new(int)
	*p = 3
	fmt.Println("*p = ", *p)

	// c type approach
	var p2 *int
	var n int = 5
	p2 = &n //assigning address of n to pointer p2
	fmt.Println("*p2 = ", *p2)
}
