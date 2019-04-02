package main

import "fmt"

func main() {

	var appint int
	fmt.Print(" enter value : ")
	num, err := fmt.Scan(&appint)

	fmt.Println("input value is : ", appint)
	fmt.Println("number of input :  ", num)
	fmt.Println("error in scanf : ", err) //input other than int
}
