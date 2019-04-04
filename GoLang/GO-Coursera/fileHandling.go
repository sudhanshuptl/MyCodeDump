package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	// simply open the file read file and close
	// so obviously not good for large files
	// data_bytes is bite array contain all file
	data_bytes, err := ioutil.ReadFile("./GoLang/GO-Coursera/loop.go")

	// writing file first is filename then data in bytes format then file permission in unix style
	//err := ioutil.WriteFile("filename",data_bytes, "0777")

	if err == nil {
		fmt.Println(string(data_bytes))
	} else {
		fmt.Println(err)
	}
}
