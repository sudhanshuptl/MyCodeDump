package main

import (
	"database/sql"

	_ "github.com/mattn/go-sqlite3" // _ It's for importing a package solely for its side-effects.
	// Since go does not allow a package without any direct use this is a bypass for such cases
)

func main() {
	db, _ := sql.Open("sqlite3", "./go.db")
	statement, _ := db.Prepare("create table if not exists people (id Integer primary key, name text)")

	statement.Exec()

	statement, _ = db.Prepare("insert into people (name ) values (?)")

	statement.Exec("ROhan Patel")

}
