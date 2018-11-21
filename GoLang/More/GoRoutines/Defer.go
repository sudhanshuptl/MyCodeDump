package main

import (
	"fmt"
	"sync"
	"time"
)

func foo(){
	defer fmt.Println("It will mandatory execute after completion of this func")
	defer fmt.Println("This is one more defer,  it will execute before above defer as it follow bottom top defer statement order")
	fmt.Println("It does some stuff ")
}

var waitGroup sync.WaitGroup

func doISay(s string){
	defer waitGroup.Done() // This Notify wait group that this go-routin is done and it will execute at end of this func
	// defer will run even if function panic out
	for i:=0;i<5;i++{
		fmt.Println(s)
		time.Sleep(time.Microsecond*1000)
	}
}

func main(){
	foo()
	waitGroup.Add(1)
	go doISay("hey")
	waitGroup.Add(1)
	go doISay("there")
	waitGroup.Wait()

	/*
	What happend if due to any error waitGroup.Done() does't get excuted then our program will wait forever
	Solution is panic and defer
	 */
	waitGroup.Add(1)
	go doISay("This is the end")
	waitGroup.Wait()
}