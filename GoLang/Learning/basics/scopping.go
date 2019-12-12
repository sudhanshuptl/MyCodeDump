package main

import "fmt"

var x int = 4

func main() {
	fmt.Println("x = ", x)
	f()
	fmt.Println("x = ", x)
	g()
	fmt.Println("x = ", x)
}

func f() {
	var x = 5 // this will create local x
	fmt.Println("inside f x = ", x)
}

func g() {
	x = 5 // this will override global x
	fmt.Println("inside g x = ", x)
}

// scoping rule is same as C programming
