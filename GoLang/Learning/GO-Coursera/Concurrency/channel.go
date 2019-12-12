package main

import "fmt"

/*
Transfer data between go routine
c := make(chan int)
use <- operator to send or receive
send c <- 5
receive r := <-c
*/
/*
Note: channel is unbuffered by default, so it can't hold data in transit
means sender can send data when receiver is waiting for it else sender goes to block until receiver ready to receive and voice versa
if reciver is ready but sender is not reciver will be blocked until sender is ready
blocking is same as waiting for communications
*/

func prod(v1 int, v2 int, c chan int) {
	c <- v1 * v2
}

func main() {
	c := make(chan int)
	go prod(1, 2, c)
	go prod(3, 4, c)

	a := <-c
	b := <-c
	fmt.Println("multplicstion of 4 digits are : ", a*b)

}
