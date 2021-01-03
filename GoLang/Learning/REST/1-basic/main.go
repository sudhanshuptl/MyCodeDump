package main


import (
	"fmt"
	"log"
	"net/http"
	"encoding/json"
	"github.com/gorilla/mux"
)

type Article struct{
	Title string `json:"Title"`
	Desc string `json:"desc"`
	Content string `json:"Content"`
}


type Articles []Article;

func allArticles(w http.ResponseWriter, r *http.Request){
	fmt.Println("Endpoint Hit: All article")

	articles := Articles{
		Article{Title:"Article 1", Desc: "Description1", Content:"fDummy content"},
		Article{Title:"Article 2", Desc: "Description2", Content:"fDummy content2"},
	}

	json.NewEncoder(w).Encode(articles)
	
}


func homePage(w http.ResponseWriter, r *http.Request){
	fmt.Fprint(w, "Hello World");
}

func postArticle(w http.ResponseWriter, r *http.Request){
	fmt.Fprint(w, "post article got an Hit")

}
func handleRequest(){
	myRouter := mux.NewRouter().StrictSlash(true);

	myRouter.HandleFunc("/", homePage).Methods("GET")
	myRouter.HandleFunc("/article",allArticles).Methods("GET")
	myRouter.HandleFunc("/article",postArticle).Methods("POST")

	log.Fatal(http.ListenAndServe(":8081", myRouter))
}
func main(){
	handleRequest()
}