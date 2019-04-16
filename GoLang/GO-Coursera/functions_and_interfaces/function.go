package main

import (
	"fmt"
	"sort"
)

// call by value, return 1 result
func findSum(x, y int) int { //return type is int
	return x + y
}

// call by value, return 2 result
func swap(x, y int) (int, int) {
	return y, x
}

func increment(y *int) {
	*y = *y + 1
}
func main() {
	fmt.Println("sum= ", findSum(5, 6))
	var x, y int
	x = 5
	y = 7
	x, y = swap(x, y)
	fmt.Println("swap: ", x, y)
	// call by value takes additional copying time
	fmt.Println("print y=", y)
	increment(&y)
	fmt.Println("incremented y = ", y)

	// passing array argument
	arr := [5]int{1, 2, 3, 4, 5}
	fmt.Println("first element of array: ", get_first(arr))

	//modify first by pass by pointer
	modify_first(&arr)
	fmt.Println("print first element after modification: ", arr[0])

	//in Go use slices instead of array pointer as slice by default follow memory and window technique
	// slice is basically structure contain pointer to base window location of array , length and capacity
	// in Go slices is the best option to pass array by reference
	passbyslice(arr[:])
	fmt.Println("sorted array: ", arr)

}

func get_first(arr [5]int) int {
	return arr[0]
}

func modify_first(arr *[5]int) {
	(*arr)[0] = 10
}

// pass by slice is very same to pass by reference as slice is basically reference
func passbyslice(slc []int) {
	sort.Ints(slc)
}
