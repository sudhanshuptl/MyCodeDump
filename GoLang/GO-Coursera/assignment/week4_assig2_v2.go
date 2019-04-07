package main

/*Write a program which reads information from a file and represents it
in a slice of structs. Assume that there is a text file which contains
a series of names. Each line of the text file has a first name and a last name,
in that order, separated by a single space on the line.

Your program will define a name struct which has two fields,
fname for the first name, and lname for the last name.
Each field will be a string of size 20 (characters).

Your program should prompt the user for the name of the text file.
Your program will successively read each line of the text file and
create a struct which contains the first and last names found in the file.
Each struct created will be added to a slice, and after all lines have been read
from the file, your program will have a slice containing one struct for each line
in the file. After reading all lines from the file, your program should iterate
through your slice of structs and print the first and last names found in each
struct.*/

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type name struct {
	fname string
	lname string
}

func main() {

	/*
		Example names and surnames to put in file: ~/names.txt

		Tiera Guinn
		Marie Curie
		Elizabeth Blackwell
		Jane Goodall
		Mae Jemison
		Jennifer Doudna
		Katherine Freese
		Rachel Carson
		Maria Mayer
		Sara Seager

	*/
	fmt.Println("Enter the path of file: ")
	scan := bufio.NewScanner(os.Stdin)
	scan.Scan()
	names := scan.Text()
	fmt.Println(names)
	file, _ := os.Open(names)

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	var txtlines []string

	for scanner.Scan() {
		txtlines = append(txtlines, scanner.Text())

	}

	file.Close()

	nameSlice := make([]name, 0, len(txtlines))

	for _, v := range txtlines {
		someString := v
		words := strings.Fields(someString)
		fmt.Println(words[0], words[1])
		nameSlice = append(nameSlice, name{words[0], words[1]})
	}

	for _, j := range nameSlice {
		fmt.Println(j.fname, j.lname)
	}

}
