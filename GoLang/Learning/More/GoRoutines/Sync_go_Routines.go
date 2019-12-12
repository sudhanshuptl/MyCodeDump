package main

import (
	"fmt"
	"sync"
	"time"
)

var waitGroup sync.WaitGroup

func doSay(s string){
	for i:=0;i<5;i++{
		fmt.Println(s)
		time.Sleep(time.Microsecond*1000)
	}
	waitGroup.Done() // This Notify wait group that this go-routin is done
}

func main() {
	waitGroup.Add(1)
	go doSay("hey")
	waitGroup.Add(1)
	go doSay("there")
	waitGroup.Wait()

	/*
	What happend if due to any error waitGroup.Done() does't get excuted then our program will wait forever
	Solution is panic and defer
	 */
	waitGroup.Add(1)
	go doSay("This is the end")
	waitGroup.Wait()


}