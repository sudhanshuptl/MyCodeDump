package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

type Name struct {
	fname string
	lname string
}

func main() {
	var fileName string
	fmt.Print("Enter file name: ")
	_, _ = fmt.Scanf("%s", &fileName)

	data_bytes, err := ioutil.ReadFile(fileName)
	if err != nil {
		fmt.Println(err)
		os.Exit(-1)
	}

	dataStr := strings.Split(string(data_bytes), "\n")

	slc := make([]Name, 0, 5)

	for _, data := range dataStr {
		nameSplit := strings.Split(data, " ")
		slc = append(slc, Name{fname: nameSplit[0], lname: nameSplit[1]}) //appending new data to slice
	}

	//printing all data from slice
	for _, name := range slc {
		fmt.Printf("fname: %s, lname: %s \n", name.fname, name.lname)
	}

}
