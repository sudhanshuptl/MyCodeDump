package main

import "fmt"

type Employee struct {
	name  string
	empId int
}

func main() {

	// aggregate data type
	// group together arbitrary data type to one type

	var emp1 Employee
	emp1.name = "Sudhanshu"
	emp1.empId = 3543

	fmt.Printf("%s : %d", emp1.name, emp1.empId)

	// create and initialize struct element to 0
	emp2 := new(Employee)
	fmt.Printf("\n%s : %d", emp2.name, emp2.empId)

	//initialize with values
	emp3 := Employee{name: "Sudhanshu", empId: 45656}
	fmt.Printf("\n%s : %d", emp3.name, emp3.empId)

}
