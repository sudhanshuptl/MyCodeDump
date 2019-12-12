package main

/*
Race condition is an event that happens when separate parts of a running program access shared data,
which leads to an outcome that cannot be determined before running it.
Here race condition exist because both tries to modify account balance  simultaneously
So result will be unpredictable as we are not sure about what is final overridden value

Here final account balance should be 150 but it is un-deterministic here
initial balance :100
Added = +100
withdraw = -50
final= should be 150 but un-deterministic here because of race condition
*/

import (
	"fmt"
	"time"
)

var accountBalance = 100

func creditAccount(amount int) {
	var i int
	for i = 1; i <= amount; i++ {
		accountBalance += 1 // adding 1 sat a time instead of whole amount at once
		time.Sleep(10 * time.Millisecond)
	}
}

func debitAccount(amount int) {
	var i int
	for i = 1; i <= amount; i++ {
		accountBalance -= 1 // subtracting 1 sat a time instead of whole amount at once
		time.Sleep(100 * time.Millisecond)
	}
}

func main() {
	fmt.Println("Account balance before any debit or credit: ", accountBalance)

	// debit
	go debitAccount(50)
	// adding 100
	go creditAccount(100)

	time.Sleep(1000 * time.Millisecond)

	fmt.Println("closing balance after adding 100 and withdrawing 50 , final account Balance:", accountBalance)
}
