package main

import "fmt"

func fib(n int) chan int {
	out := make(chan int)

	//Ananoums function running as go routine that is adding next fib number to channel
	go func() {
		// We need to close channel when this method completes else it will create deadlocl
		//fatal error: all goroutines are asleep - deadlock!
		defer close(out)

		// list comprehention kind of synatx here
		for i, j := 0, 1; i < n; i, j = i+j, i {
			out <- i
		}
	}() // calling this ananoumous function

	return out
}

func main() {
	// fetching data from channlel
	for val := range fib(100) {
		fmt.Println(val)
	}

}
