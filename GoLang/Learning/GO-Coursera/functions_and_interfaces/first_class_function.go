package main

import "fmt"

//function can be treated as any other types
// so variable can be declared as a function type
// can be created dynamically

func main() {
	var mysum func(int, int) int
	mysum = add
	fmt.Println("sum: ", mysum(4, 5))
	// we can also define anonymous function
	mysum = func(i int, i2 int) int {
		return i + i2
	}
	fmt.Println("sum: ", mysum(5, 5))
}

func add(a int, b int) int {
	return a + b
}

// a function can return a function
//we can pass a function to other function, obviously function+its environment also passed concept of closer

// Golang follow lexical scopping
