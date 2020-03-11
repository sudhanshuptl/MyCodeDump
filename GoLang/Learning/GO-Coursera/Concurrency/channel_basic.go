package main
import (
	"fmt"
	"time"
)
func printCount(c chan int) {
	num := 0
	for num >= 0 {
		num = <-c
		fmt.Print(num, " ")
	}
}
func main() {
	c := make(chan int)
	a := []int{8, 6, 7, 5, 3, 0, 9, -1}
	go printCount(c)
	// Iterating over a and putting values to channel that is concurrently process by printCount
	for _, v := range a {
		c <- v
	}
	time.Sleep(time.Millisecond * 1)
	fmt.Println("End of main")
}