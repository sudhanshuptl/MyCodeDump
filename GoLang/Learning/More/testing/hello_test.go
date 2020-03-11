package main

import "testing"

// Name convention should be like fileToTest_test.go
// run : go test

func TestName(t *testing.T) {
	name := getName()
	if name != "World!" {
		t.Error("Respone from getName is unexpected value")
	}
}