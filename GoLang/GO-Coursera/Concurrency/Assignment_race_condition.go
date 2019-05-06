package main

import (
	"fmt"
	"time"
)

/*
Race condition is an event that happens when separate parts of a running program access shared data, which leads to an outcome that cannot be determined before running it.
There are two operations that are taking place, the value printed depend on which of these two operations completes first.
*/

var number int

func main() {

	go goRoutine()
	go goRoutine()
	time.Sleep(1000 * time.Millisecond)
}

func goRoutine() {
	for i := 0; i < 100; i++ {
		number = i
		fmt.Println(number)
	}
}
