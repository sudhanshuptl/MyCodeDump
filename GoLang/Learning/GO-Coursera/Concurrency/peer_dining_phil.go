package main

import (
	"fmt"
	"sync"
)

type chopS struct {
	sync.Mutex
}

type Philo struct {
	leftCS  *chopS
	rightCS *chopS
}

var wg sync.WaitGroup

func host(p []*Philo) {
	for i := 0; i < 5; i++ {
		go p[i].eat(i + 1)
	}
}

func (p Philo) eat(philosopherNumber int) {
	for i := 3; i > 0; i-- {
		p.leftCS.Lock()
		p.rightCS.Lock()
		fmt.Println("Starting to eat ", philosopherNumber)
		fmt.Println("Finishing Eating ", philosopherNumber)
		p.rightCS.Unlock()
		p.leftCS.Unlock()
	}
	wg.Done()
}

func main() {
	wg.Add(5)
	cSticks := make([]*chopS, 5)
	for i := 0; i < 5; i++ {
		cSticks[i] = new(chopS)
	}
	fmt.Println()
	philos := make([]*Philo, 5)
	for i := 0; i < 5; i++ {
		philos[i] = &Philo{cSticks[i], cSticks[(i+1)%5]}
	}
	go host(philos)
	wg.Wait()
}