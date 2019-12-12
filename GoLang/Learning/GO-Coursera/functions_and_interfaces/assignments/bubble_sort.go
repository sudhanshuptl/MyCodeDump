package main

import (
	"fmt"
	"os"
)

func main() {
	var n int //number of integer
	var arr [10]int
	fmt.Print("Enter number of integer: ")
	_, err := fmt.Scan(&n)

	if err != nil {
		fmt.Println(err)
		os.Exit(-1)
	}

	if n > 10 {
		fmt.Println("Please Max 10 values are allowed")
		os.Exit(-1)
	}

	fmt.Printf("Please enter %d integers :", n)
	for i := 0; i < n; i++ {
		_, err := fmt.Scan(&arr[i])

		if err != nil {
			fmt.Println(err)
			os.Exit(-1)
		}
	}

	fmt.Println("Before sorting :", arr[:n])
	BubbleSort(arr[:n])
	fmt.Println("After Bubble sort:", arr[:n])

}

//Bubble sort
func BubbleSort(slc []int) {
	length := len(slc)
	for i := 0; i < length; i++ {
		for j := 0; j < length-i-1; j++ {
			if slc[j] > slc[j+1] {
				swap(slc, j)
			}
		}
	}

}

// swap
func swap(a []int, j int) {
	var temp int
	temp = a[j]
	a[j] = a[j+1]
	a[j+1] = temp
}
