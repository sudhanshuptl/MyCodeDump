package main

import "fmt"

func main() {
	var acceleration, initV, initD, time float64
	fmt.Print("Please Enter Initial Displacement: ")
	_, _ = fmt.Scan(&initD)
	fmt.Print("Please Enter Initial velocity: ")
	_, _ = fmt.Scan(&initV)
	fmt.Print("Please Enter Acceleration: ")
	_, _ = fmt.Scan(&acceleration)

	findDisplacement := GenDisplaceFn(initV, initD, acceleration)

	fmt.Print("Please Enter time: ")
	_, _ = fmt.Scan(&time)

	fmt.Printf("Displacemetnt in given time %f is := %f ", time, findDisplacement(time))

}

func GenDisplaceFn(velocity, in_disp, acc float64) func(float64) float64 {
	return func(time float64) float64 {
		return (1/2)*acc*time*time + velocity*time + in_disp
	}
}
