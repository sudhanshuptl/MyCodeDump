package main

import (
	"fmt"
	"sync"
	"time"
)

var waitGroup sync.WaitGroup

func doSay(s string){
	defer 	waitGroup.Done() // This Notify wait group that this go-routin is done
	defer cleanup() //when panic occur this will help to recover
	for i:=0;i<5;i++{
		fmt.Println(s)
		time.Sleep(time.Microsecond*1000)
		if i == 2{
			panic("Oh shit i is 2 now")
		}
	}
}

func cleanup(){
	if r := recover(); r != nil{ // if there is no panic situation then recover return nil
		fmt.Println("Recovered in cleanup :", r)
	}
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