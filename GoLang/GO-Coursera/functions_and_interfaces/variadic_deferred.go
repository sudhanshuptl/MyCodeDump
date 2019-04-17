package main

import "fmt"

// how to tak variable number of arguments
// we can use ... to specify variable number of arguments

func getMax(vals ...int) int { //it can take any number of integer
	maxV := -1
	for i := 0; i < len(vals); i++ {
		if vals[i] > maxV {
			maxV = vals[i]
		}
	}
	return maxV
}

func main() {
	defer fmt.Println("Bye !")
	fmt.Println("Max is : ", getMax(4, 3, 5, 2, 5, 2, 4, 3))

	slc := []int{4, 3, 5, 2, 5, 2, 4, 3, 89} // or we can create a slice e and then pass
	fmt.Println("Max is : ", getMax(slc...)) //... is necessary to specify unpack and pass
	testDefered()
}

// deferred function called at end of function
// so mostly used for cleanup
// defer executed immediately but printed at end Ex

func testDefered() {
	i := 1
	defer fmt.Println("defer printing i:", i)
	i++
	//since defered thing should executed after i++ so its value sholud be 2 but in reality it will be 1
}
