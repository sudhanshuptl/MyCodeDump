package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var st string
	var flag bool = false

	fmt.Println("Input String: ")
	//num, err := fmt.Scanf("%s",&st)
	in := bufio.NewReader(os.Stdin)
	st, err := in.ReadString('\n')

	// check for error
	if err != nil {
		fmt.Println("Error while reading data : ", err)
		return
	}
	fmt.Println("Input string is : ", st)

	// convert to lower case and strip \n from the end
	st = strings.ToLower(st[:len(st)-1])

	if st[0] != 'i' || st[len(st)-1] != 'n' {
		flag = false
	} else {
		if strings.Contains(st, "a") {
			flag = true
		}
	}

	if flag {
		fmt.Println("Found!")
	} else {
		fmt.Println("Not Found!")
	}

}

//
//func main() {
//	fmt.Printf("Enter a string: ")
//	// I could not get fmt.Scan working, so used bufio.Scanner
//	scanner := bufio.NewScanner(os.Stdin)
//	if scanner.Scan() {
//		str := strings.ToLower(scanner.Text()) // get the input and ignore case
//		if strings.HasPrefix(str, "i") && strings.HasSuffix(str, "n") && strings.ContainsAny(str, "a") {
//			fmt.Println("Found!")
//		} else {
//			fmt.Println("Not Found!")
//		}
//	} else {
//		fmt.Println("Something went wrong with the input!")
//	}
// }
