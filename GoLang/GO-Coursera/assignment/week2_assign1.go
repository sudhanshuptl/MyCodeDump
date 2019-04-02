package main

import "fmt"

func main() {
	var input_float float32
	fmt.Print("Enter floating point number : ")
	num, err := fmt.Scan(&input_float)

	// check for error
	if err != nil {
		fmt.Println("Error while reading data : ", err, "number of inout : ", num)
		return
	}

	//Typecast to integer and print
	fmt.Println("Truncated integer : ", int(input_float))
}
