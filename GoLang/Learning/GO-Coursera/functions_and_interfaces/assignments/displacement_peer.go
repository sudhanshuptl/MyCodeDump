package main

import (
	"fmt"
)

func GenDisplaceFn(acc, vel, s0 float32) func(time float32) float32 {
	return func(time float32) float32 {
		var s1 float32
		s1 = 0.5*acc*time*time + vel*time + s0
		return s1
	}
}

func main() {
	var a, v, s, t float32
	fmt.Print("Enter the accerlation:")
	fmt.Scan(&a)
	fmt.Print("Enter the velocity:")
	fmt.Scan(&v)
	fmt.Print("Enter the initial displacement:")
	fmt.Scan(&s)
	fn := GenDisplaceFn(a, v, s)
	fmt.Print("Enter the time:")
	fmt.Scan(&t)
	fmt.Println(fn(t))
}
