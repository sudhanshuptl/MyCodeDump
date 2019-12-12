package Introduction_to_go

import "fmt"

func main() {
	// default value for array is automatically assignedthat will be equivalent to 0 in that data datatype
	// fixed length array
	var arr1 [5]int
	fmt.Println("Default initialisation", arr1)

	var arr2 [5]int = [5]int{1, 2, 3, 4, 5}
	fmt.Println("direct assignment", arr2)

	y := [7]int{2, 3, 4, 5, 6, 7, 8}
	fmt.Println("implicit direct assignment", y)

	// does not specify exact size
	z := [...]int{2, 3, 4, 5, 6, 7, 8, 10, 10, 11}
	fmt.Println("implicit direct assignment", z)

	//loop over array
	for i, v := range z {
		fmt.Println("index: ", i, "value: ", v)
	}
}
