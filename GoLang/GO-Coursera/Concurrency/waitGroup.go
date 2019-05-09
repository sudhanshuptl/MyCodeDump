package main

import (
	"fmt"
	"sync"
)

// In GO , go main thread always associate with main function
// and main function can terminate before all go routine to be completed
// SO We can use waitGroup to ensure that

func newRoutine(wg *sync.WaitGroup) {
	fmt.Println("New Routine")
	wg.Done()
}

func main() {
	var wg sync.WaitGroup

	wg.Add(1)          // add go number routine in action
	go newRoutine(&wg) //goRoutine
	wg.Wait()          //wait for all go routine to complete
	fmt.Println("go routine is completed so no need to wait exiting")

}
