package Introduction_to_go

import "fmt"

func main() {
	var y *int
	y = f()
	fmt.Println("y = ", *y)
}

// Here ideally in any other programming language x should be destroyed after function completion as it generally stored in stack area
// but in case of pointer it is difficult as this scenario is possible
func f() *int {
	x := 5
	return &x
}
