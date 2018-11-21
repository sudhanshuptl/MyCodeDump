package main

import (
	"fmt"
	"time"
)

func say(s string){
	for i:=0;i<5;i++{
		fmt.Println(s)
		time.Sleep(time.Microsecond*1000)
	}
}

func main(){
	go say("hey")
	go say("there")
	//time.Sleep(time.Second)
	/*
	If we want both function to complete make sure main thread does't stop before completion of go routing
	that is why if both are go routing no one is blocking main thread to stop completion so no result will be produced
	go say("hey")
	go say("there")

	if we want it to work add some blocking method after that like time.Sleep(time.Second)
	best way to do that is synchronise go routine
	 */
}