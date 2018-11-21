package main

import (
	"fmt"
	"html/template"
	"net/http"
)


type myPage struct {
	Title string
	Body string
}
func main()  {
	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/home/",myHandler)
	http.ListenAndServe(":8000", nil)
}

func indexHandler(w http.ResponseWriter, r *http.Request){
	fmt.Fprintf(w,"<h2> Hello, World! </h2>")
}

func myHandler(w http.ResponseWriter, r *http.Request){
	p := myPage{Title: "My page Title", Body: "This body of the page"}
	t, err := template.ParseFiles("./basicTemplate.html")
	if err != nil{
		fmt.Println("Error occured while Parsing :",err)
	}
	err = t.Execute(w, p)
	if err != nil{
		fmt.Println("Error occured while rendering :",err)
	}

}