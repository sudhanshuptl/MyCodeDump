package main

import (
	"fmt"
)


func foo(c chan int,someValue int){
	c  <- someValue *5 // <- channel operator
}
func main(){
	myChan := make(chan int)
	go foo(myChan, 5)
	go foo(myChan, 3)
	go foo(myChan, 10)

	// channel is blocking so it wait to complete
	v1 := <-myChan
	v2 := <-myChan
	v3 := <-myChan
	// order of output is not maintained in chanel it depend on order of completion of func
	fmt.Println(v1, v2, v3)
	}
