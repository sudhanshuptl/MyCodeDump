package main

import (
	"fmt"
)


func foo(c chan int,someValue int){
	c  <- someValue *5 // <- channel operator
}
func main(){
	myChan := make(chan int)

	for i:=0; i<10; i++{
		go foo(myChan, i)
	}
	for item := range myChan{
		fmt.Println(item)
	}
}
