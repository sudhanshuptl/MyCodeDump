package main

import (
	"fmt"
	"net/http"
)

func main(){
	/* this function is called by default like init in python */
	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/about", aboutHandler)
	http.ListenAndServe("localhost:8000", nil)
}

func indexHandler(w http.ResponseWriter, r *http.Request){
	fmt.Fprintf(w, "Wow go is Awesome")
}

func aboutHandler(w http.ResponseWriter, r *http.Request){
	fmt.Fprintf(w, "This is Sudhanshu Patel")
}

/* There is no classes in go , so we have to work with struct only */