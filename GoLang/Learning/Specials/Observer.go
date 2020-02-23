package main

import (
	"fmt"
	"sync"
	"time"
)

/*
 Observers are the system that is looking for changes at things they are monitoring
 in this case it is fibonacci channel
*/

type (
	Event struct {
		// this will be data type that is send to observer when fib generator generate a number
		data int
	}

	Observer interface {
		NotifyCallback(Event)
	}

	Subject interface {
		// Open interface that any structure can implement
		AddListner(Observer)
		RemoveListner(Observer)
		Notify(Event)
	}

	eventObserver struct {
		// will implement it with Observer type
		id   int
		time time.Time
	}

	eventSubject struct {
		// will implement this with Subject type
		observers sync.Map
	}
)

// implementing
func (e *eventObserver) NotifyCallback(event Event) {
	// We recieved the data in channel after this amount of time
	fmt.Printf(" Recieved : %d after %v \n", event.data, time.Since(e.time))
}

func (s *eventSubject) AddListner(obs Observer) {
	// store in a map as empty anonymous struct as its values
	// if an observer is in this map then it is being listen else not
	s.observers.Store(obs, struct{}{})
}
func (s *eventSubject) RemoveListner(obs Observer) {
	// delete an obs key from dict
	s.observers.Delete(obs)
}

func (s *eventSubject) Notify(event Event) {
	s.observers.Range(
		func(key interface{}, value interface{}) bool {
			if key == nil || value == nil {
				// termination condition
				return false
			}
			// convert key from interface to Observer
			key.(Observer).NotifyCallback(event)
			return true
		})
}

func fibb(n int) chan int {
	out := make(chan int)

	//Ananoums function running as go routine that is adding next fib number to channel
	go func() {
		// We need to close channel when this method completes else it will create deadlocl
		//fatal error: all goroutines are asleep - deadlock!
		defer close(out)

		// list comprehention kind of synatx here
		for i, j := 0, 1; i < n; i, j = i+j, i {
			out <- i
		}
	}() // calling this ananoumous function

	return out
}

func main() {
	n := eventSubject{observers: sync.Map{}}
	var obs1 = eventObserver{id: 1, time: time.Now()}
	var obs2 = eventObserver{id: 1, time: time.Now()}

	n.AddListner(&obs1)
	n.AddListner(&obs2)

	for x := range fibb(100) {
		n.Notify(Event{data: x}) // creates a new event with data
		// we get all results twice because each time oth observer are notified with same data in channel
	}
}
