package main

import "fmt"

type myInt int
type myIntP int

// define doubleIT function associated with type myInt
//first bracket represent receiver type and it is implicitly passed
func (mi myInt) doubleIt() myInt {
	mi = mi * 2
	return mi
}

func (mi *myIntP) doubleIt() {
	*mi = *mi * 2
	// no need to write * for structure pointer as it dereference automatically
}
func main() {
	// We can only define function associated with a type in same file only
	// so we can not define function for implicit types like int

	v := myInt(5)
	fmt.Println("V :=", v, " Double V := ", v.doubleIt())

	//struct and function associated with it togather give the idea of classes in go

	//We can use this to have controlled access to data
	//by defining structure and methods in other file then acessing it in main using just function names
	// as variables directly not accessible

	// receiver  variable is a copy of actual variable so update can't reflect in original
	fmt.Println("V :=", v, " Double V := ", v.doubleIt())

	vp := myIntP(3)
	fmt.Println("V :=", vp)
	//automatically pass pointer
	vp.doubleIt() //changes reflect in original variable
	fmt.Println(" Double V := ", vp)
}
