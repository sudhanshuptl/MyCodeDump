package main

import "fmt"

func main() {
	for i := 0; i < 5; i++ {
		fmt.Println("loop type 1 : ", i)
	}

	i := 0
	for i < 5 {
		fmt.Println("loop type 2: ", i)
		i++
	}

	count := 0
	for {
		fmt.Println("loop type 3")
		count++
		if count == 5 {
			break
		}
	}
}
