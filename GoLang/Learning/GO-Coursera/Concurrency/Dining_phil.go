package main

import (
	"fmt"
	"sync"
)


// Philosopher represented by number
type Philosopher struct {
	num int
}

// Chopstick would be later put into a pool
type Chopstick struct {
}


// create a pool of 5 chopstick
var pool = sync.Pool{
	New: func() interface{} {
		return new(Chopstick)
	},
}

var w sync.WaitGroup

func (p Philosopher) eat(host chan int) {
	defer w.Done()

	// get permission from the host
	// it also ensure to enable to restriction,  two philosopher at a time
	// as host has buffer size of 2
	<-host

	fmt.Printf("starting to eat %d\n", p.num)
	// pick up chopsticks in any order
	left := pool.Get()
	right := pool.Get()
	// then return the chopsticks
	pool.Put(left)
	pool.Put(right)
	fmt.Printf("finishing eating %d\n", p.num)

	host <- 1
}

func hostRoutine(host chan int){
	defer w.Done()
	host <- 1
	host <- 1
}

func main() {
	// host allows no more than 2 philosophers to eat concurrently
	host := make(chan int, 2)

	// initialize chopsticks pool
	for i := 0; i < 5; i++ {
		pool.Put(new(Chopstick))
	}

	// initialize philosophers
	philosophers := make([]*Philosopher, 5)
	for i := 0; i < 5; i++ {
		// Add a philosopher and number them , 1 through 5
		philosophers[i] = &Philosopher{i + 1}
	}

	// let them start
	for i := 0; i < 5; i++ {
		for j := 0; j < 3; j++ { // only eat 3 times
			w.Add(1)
			go philosophers[i].eat(host)
		}
	}

	// This will ensure only two philosopher can eat at a time
	w.Add(1)
	go hostRoutine(host)

	// it ensure wait till all go routine get completed
	w.Wait()
}