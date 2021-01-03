package main

import (
	"fmt"
)

func Calculation(x int)(result int){
	result = x+2
	return result
}

func main(){
	fmt.Println("Go testing tutorial")
	result := Calculation(2)
	fmt.Println(result)
}