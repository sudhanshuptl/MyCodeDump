package main

import "fmt"

func main() {

	arr := [...]int{10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

	// slice is window on an array so it will be a subset of a array
	//slice have three features
	// pointer  : start position of slice
	// length (len()): length of a slice
	//capacity (cap()): maximum capacity of slice , it can go max till end of array
	sl := arr[2:5]
	fmt.Println("length of slice: ", len(sl), "capacity of slice: ", cap(sl), "slice : ", sl)

	// writing to a slice override underlying array and other slice that is accessing same window
	sl[0] = 100000
	fmt.Println("override slice : ", sl, "\noverride parent array : ", arr)

	// if you are creating a slice using slice literal it will create an underline array and then create a slice of that array

	// create slice using implicit assignment
	// if we do not specify anything in [] compiler assume this must be a slice
	slc := []int{5, 6, 3, 7, 8, 9, 0}
	fmt.Println("slice : ", slc)

	// create slice using make(type, length, capacity[non mandatory])
	// if capacity is more than length means size of underlying array is more then size of slice means
	// slice capacity > slice length

	sl_new := make([]int, 5, 10)
	fmt.Println("length of slice: ", len(sl_new), "length of underline array: ", cap(sl_new))

	// creating slice with capacity  == length means undelying array will have same length
	sl_s := make([]int, 5)
	fmt.Println("length of slice: ", len(sl_s), "length of underline array: ", cap(sl_s))

	// we can append element in slice that simply insert element in underlying array
	// we can also append beyond the size of underlying array but obviously time cast will be there
	// as it involve creation of new array and slice variable start pointing to new array

	arr3 := [...]int{10, 11, 12, 13}
	sl_s = arr3[:] //  create slice
	fmt.Println("array before appending in slice ", arr3)
	sl_s = append(sl_s, 5500)
	sl_s = append(sl_s, 5501)

	fmt.Println("New slice : ", sl_s)
	fmt.Println("New array will be: ", arr3) // old array remains same as slice start point to new copy of array with appended value

}
