package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
)

type Person struct {
	Name    string `json:"name"`
	Address string `json:"address"`
}

func main() {
	var person Person

	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter the Name : ")
	name, _ := reader.ReadString('\n')

	person.Name = name[:len(name)-1]

	fmt.Print("Enter the Address : ")
	address, _ := reader.ReadString('\n')

	person.Address = address[:len(address)-1]

	jn, _ := json.MarshalIndent(person, "", "    ")

	fmt.Println(string(jn))

}
