package main

import (
	"encoding/json"
	"fmt"
	"github.com/gorilla/mux"
	"net/http"

	"github.com/jinzhu/gorm"
	_"github.com/jinzhu/gorm/dialects/sqlite"

)

var db *gorm.DB
var err error

type User struct {
	gorm.Model
	Name  string
	Email string
}

func InitialMigration() {
	db, err = gorm.Open("sqlite3", "mydb.db")
	if err != nil {
		fmt.Println(err.Error())
		panic("Failed to connect to DB")
	}
	defer db.Close()

	db.AutoMigrate(&User{})
}

func AllUsers(w http.ResponseWriter, r *http.Request) {
	// http://localhost:8081/users/
	db, err = gorm.Open("sqlite3", "mydb.db")
	if err != nil {
		fmt.Println(err.Error())
		panic("Failed to connect to DB")
	}
	defer db.Close()

	var users []User
	db.Find(&users) // Query on database and put the results in users
	json.NewEncoder(w).Encode(users) // encode results in writer


}

func NewUser(w http.ResponseWriter, r *http.Request) {
	//http://localhost:8081/users/Akash/aks@gmail.com
	db, err = gorm.Open("sqlite3", "mydb.db")
	if err != nil {
		fmt.Println(err.Error())
		panic("Failed to connect to DB")
	}
	defer db.Close()

	values := mux.Vars(r)
	name := values["name"]
	email := values["email"]
	db.Create(&User{Name: name, Email: email})

	fmt.Fprintf(w, "New User Successfully added")

}

func DeleteUser(w http.ResponseWriter, r *http.Request) {
	//http://localhost:8081/users/Akash
	db, err = gorm.Open("sqlite3", "mydb.db")
	if err != nil {
		fmt.Println(err.Error())
		panic("Failed to connect to DB")
	}
	defer db.Close()

	values := mux.Vars(r)
	name := values["name"]

	var user User
	db.Where("name = ?", name).Find(&user)
	db.Delete(&user)
	fmt.Fprintf(w, "User Succesfully deleted")
}

func UpdateUser(w http.ResponseWriter, r *http.Request) {
	//http://localhost:8081/users/Akash/Akash@amdoc.com
	db, err = gorm.Open("sqlite3", "mydb.db")
	if err != nil {
		fmt.Println(err.Error())
		panic("Failed to connect to DB")
	}
	defer db.Close()

	values := mux.Vars(r)
	name := values["name"]

	var user User
	db.Where("name = ?", name).Find(&user)
	user.Email = values["email"]

	db.Save(&user)

	fmt.Fprintf(w, "User Succesfully Updated")
}
