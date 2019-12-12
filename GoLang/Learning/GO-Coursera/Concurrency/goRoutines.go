package main

import (
	"fmt"
	"time"
)

/*
Race condition is an event that happens when separate parts of a running program access shared data, which leads to an outcome that cannot be determined before running it.
There are two operations that are taking place, the value printed depend on which of these two operations completes first.
*/

var num1 int

func main() {

	go changeVal()
	go changeVal()
	time.Sleep(1000 * time.Millisecond)
}

func changeVal() {
	for i := 0; i < 100; i++ {
		num1 = i
		fmt.Println(num1)
	}
}
