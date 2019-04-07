package main

import (
	"fmt"
	"sort"
	"strconv"
)

func main() {
	// create empty slice of size 3
	slc := make([]int, 3)
	index := 0
	var inp string
	var n int

	for {
		fmt.Print("Enter next number : ")
		_, err := fmt.Scanf("%s", &inp)
		if err != nil {
			println("Error while reading data", err)
			continue
		}

		if inp == "X" {
			break
		} else {
			n, err = strconv.Atoi(inp)
			if err != nil {
				fmt.Println("Error While converting input to int : ", err)
				fmt.Println("Please input 'X' if you want to exit ")
				continue
			}
		}
		if index < len(slc) {
			slc[index] = n
		} else {
			slc = append(slc, n)
		}
		index++

		// sorting slice
		sort.Ints(slc[:index])
		//printing only used data of slice
		fmt.Println("Sorted Slice : ", slc[:index])
	}
}
