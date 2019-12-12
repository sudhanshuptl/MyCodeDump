package main

import (
	"fmt"
	"strings"
)

type Animal interface {
	Eat()
	Move()
	Speak()
}

type Cow struct {
	food, locomotion, noise string
}

func (c Cow) Eat() {
	fmt.Println(c.food)
}

func (c Cow) Speak() {
	fmt.Println(c.noise)
}

func (c Cow) Move() {
	fmt.Println(c.locomotion)
}

type Snake struct {
	food, locomotion, noise string
}

func (s Snake) Eat() {
	fmt.Println(s.food)
}

func (s Snake) Speak() {
	fmt.Println(s.noise)
}

func (s Snake) Move() {
	fmt.Println(s.locomotion)
}

type Bird struct {
	food, locomotion, noise string
}

func (b Bird) Eat() {
	fmt.Println(b.food)
}

func (b Bird) Speak() {
	fmt.Println(b.noise)
}

func (b Bird) Move() {
	fmt.Println(b.locomotion)
}

func main() {
	animals := make(map[string]Animal)

	for {
		// TODO: write command logic for commands newanimal and create
		fmt.Println("What do you want to do? \n <command[newanimal,query]> <name_of_animal> <type of animal or action [(cow,bird,snack), (eat,speak,move)]>")
		var command, name, actionOrKind string
		fmt.Print(" >")
		fmt.Scan(&command, &name, &actionOrKind)
		command = strings.ToLower(command)
		name = strings.ToLower(name)
		actionOrKind = strings.ToLower(actionOrKind)

		if command == "newanimal" {
			switch actionOrKind {
			case "cow":
				animals[name] = Cow{"grass", "walk", "moo"}
			case "bird":
				animals[name] = Bird{"worms", "fly", "peep"}
			case "snake":
				animals[name] = Snake{"mice", "slither", "hsss"}
			default:
				fmt.Println("Animal type mismatch : please use  (cow,bird,snake)")
				continue
			}
			fmt.Println("Created it!")
		} else if command == "query" {
			switch actionOrKind {
			case "eat":
				animals[name].Eat()
			case "speak":
				animals[name].Speak()
			case "move":
				animals[name].Move()
			}
		} else {
			fmt.Println("Invalid command [newanimal, query]")
		}
	}
}
