package Introduction_to_go

import (
	"fmt"
)

func main() {
	var x int
	fmt.Print("Enter value of x :")
	fmt.Scanf("%d", &x)
	switch x {
	case 1:
		fmt.Print("case 1 ")
	case 2:
		fmt.Println("case 2")
	case 3:
		fmt.Println("case 3")
	default:
		fmt.Println("default")

	}
	y := -4
	// Tagless switch
	switch {
	case x > 1:
		fmt.Println("x >1")
	case y < 0:
		fmt.Println("y <0 ")
	default:
		fmt.Println("default case")

	}
}
