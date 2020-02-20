package main

/*
Print all prime number before given value N
 */


/*
// Sample code to perform I/O:

fmt.Scanf("%s", &myname)            // Reading input from STDIN
fmt.Println("Hello", myname)        // Writing output to STDOUT

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
*/
import (
	"fmt"
	"math"
)
// Write your code here
func isPrime(x int) bool{
	sqrtR := int(math.Sqrt(float64(x))) + 1
	if x%2 ==0{
		return false
	}
	for i:=3; i< sqrtR; i = i+2{
		if x%i == 0 {
			return false
		}
	}
	return true
}

func main(){
	var limit int
	_, _ = fmt.Scanf("%d", &limit)

	for i:=2; i<= limit; i++{
		if isPrime(i) {
			fmt.Printf("%d ", i)
		}
	}
}
