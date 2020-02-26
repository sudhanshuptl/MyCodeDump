package main

import (
	"net/http"
)

const msg = "This is a Hello World msg"

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "text/plain; charset=utf-8")
		w.WriteHeader(http.StatusOK)
		w.Write([]byte(msg)) // convert msg to byte and add into resposewriter
	})

	http.ListenAndServe(":8080", mux)
	//run and open localhost:8080

}
