package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

//Animal struct
type Animal struct {
	food       string
	locomotion string
	noise      string
}

//Eat method
func (me *Animal) Eat() string {
	return me.food
}

//Move method
func (me *Animal) Move() string {
	return me.locomotion
}

//Speak method
func (me *Animal) Speak() string {
	return me.noise
}

//Instruct method
func (me *Animal) Instruct(command string) string {
	switch command {
	case "eat":
		return me.Eat()
	case "move":
		return me.Move()
	case "speak":
		return me.Speak()
	default:
		return fmt.Sprintf("This animal_type does not understand: %s", command)
	}
}

func readText(description string) string {
	fmt.Print(description)

	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()

	return scanner.Text()
}

func main() {
	fmt.Println("Animal questionaire.")

	animals := make(map[string]*Animal)
	animals["cow"] = &Animal{"grass", "walk", "moo"}
	animals["bird"] = &Animal{"worms", "fly", "peep"}
	animals["snake"] = &Animal{"mice", "slither", "hsss"}

	for {
		command := strings.Fields(readText("> "))
		if len(command) != 2 {
			fmt.Println("Please enter: <animal_type> <command>")
			continue
		}

		name := command[0]
		animal := animals[name]

		fmt.Println(command)
		if animal == nil {
			fmt.Printf("There is no animal_type %s.\n", name)
		} else {
			fmt.Printf("%s\n", animal.Instruct(command[1]))
		}
	}
}
