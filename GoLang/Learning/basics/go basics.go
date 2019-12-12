package main

import (
	"fmt"
	"math"
)
import "errors"


//structure
type Person struct {
	name string
	age int
}
func main() {
	x := 5 // default type decision
	var y int
	y = 9
	fmt.Println("Hello World ", x, y)

	if x > y {
		fmt.Println("x is greater than y ")
	} else if y > x {
		fmt.Println("y is greater than x")
	}
	/* Arrays */
	var arr [5] int
	fmt.Println(arr)
	arr[4] = 7
	fmt.Println(arr)
	fmt.Println("assignment of values while creating array")
	arr2 := [5]int{1, 2, 3, 4, 5}
	fmt.Println(arr2)

	fmt.Println("create Dynamic array")
	darray := []int{4, 3, 2, 1}
	fmt.Println(darray)
	darray = append(darray, 55)
	fmt.Println(darray)

	// creating a MAP
	vertics := make(map[string]int)
	vertics["id"] = 555
	vertics["km"] = 23
	fmt.Println(vertics)
	delete(vertics, "id")
	fmt.Println("after deleting a key", vertics)

	// loop
	fmt.Println("Inside loop")
	for i := 1; i < 5; i++ {
		fmt.Println("Inside for loop", i)
	}
	// using for loop as while loop
	i := 1
	for ; i < 5; {
		fmt.Println("Inside while loop", i)
		i++
	}

	// loop over each element of array
	st := []string{"sudhanshu", "patel", "India"}
	for index, value := range st {
		fmt.Println(index, value)
	}
	// looping over map values
	for key, value := range vertics {
		fmt.Println(key, value)
	}
	//calling a function
	fmt.Println("sum(3, 5) = ", sum(3, 5))

	//calling function return multiple values
	squireRoot, err := sqrt(-4)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println("squire values is := ", squireRoot)
	}

	person1 := Person{name: "Sudhanshu", age: 16}
	fmt.Println("Person data type :", person1)

	//pointer
	fmt.Println("x = ",x," its address is := ",&x)
	//increment and print
	increrment(&x)
	fmt.Println("x = ",x," its address is := ",&x)
}

func sum(x int, y int ) int{
	return x+y
}

// function can return multiple values
func sqrt(x float64) (float64, error){
	if x < 0 {
		return 0, errors.New(" Error x is less than 0")
	}
	return math.Sqrt(x), nil
}

func increrment(x *int){
	*x++
}
