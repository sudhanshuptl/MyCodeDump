package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
)

func main() {
	userData := make(map[string]string)

	fmt.Printf("Input name: ")

	scanner := bufio.NewScanner(os.Stdin)

	if scanner.Scan() {
		userData["name"] = scanner.Text()
	}

	fmt.Printf("Input address: ")

	if scanner.Scan() {
		userData["address"] = scanner.Text()
	}

	byte_array, err := json.Marshal(userData)
	if err != nil {
		fmt.Println("error:", err)
	}

	os.Stdout.Write(byte_array)
}
