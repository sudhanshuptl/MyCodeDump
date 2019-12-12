package Introduction_to_go

import (
	"encoding/json"
	"fmt"
)

type employee struct {
	Name   string
	Number int `json:"Empid"`
}

func main() {
	emp1 := employee{Name: "Sudhanshu", Number: 3454356}
	fmt.Printf("%s : %d\n", emp1.Name, emp1.Number)

	// convert it to json representation as bytes
	var jn []byte
	jn, err := json.MarshalIndent(emp1, "", "    ")

	if err != nil {
		fmt.Println("error occurred while creating json ")
	} else {
		fmt.Println(string(jn))
		var emp2 employee
		// from json byes to object
		err := json.Unmarshal(jn, &emp2)
		if err == nil {
			fmt.Printf("\n%s : %d\n", emp2.Name, emp2.Number)
		} else {
			fmt.Println(err)
		}
	}

}
