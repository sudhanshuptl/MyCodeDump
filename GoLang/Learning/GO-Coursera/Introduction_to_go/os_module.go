package Introduction_to_go

import (
	"fmt"
	"os"
)

func main() {
	// file handling using os module
	f, err := os.Open("./GoLang/GO-Coursera/loop.go")

	if err != nil {
		fmt.Println(err)
		os.Exit(-1)
	}

	//var byte_array []byte //look into it why it is not working
	// other way to do tha
	byte_array := make([]byte, 50) // we use this read 50 byte at a time max

	for {
		nb, err := f.Read(byte_array)
		if err != nil {
			break
		}
		if nb > 0 {
			fmt.Print(string(byte_array))
		}
	}
	f.Close()

}
