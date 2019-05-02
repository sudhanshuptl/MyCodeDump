package main

import (
	"fmt"
	"strings"
)

type animal struct {
	name       string
	food       string
	locomotion string
	speak      string
}

func (pet animal) Speak() string {
	return pet.speak
}

func (pet animal) Move() string {
	return pet.locomotion
}

func (pet animal) Eat() string {
	return pet.food
}

func main() {
	animals := make(map[string]animal)
	animals["cow"] = animal{name: "cow", food: "grass", locomotion: "walk", speak: "moo"}
	animals["bird"] = animal{name: "bird", food: "worms", locomotion: "fly", speak: "peep"}
	animals["snake"] = animal{name: "snake", food: "mice", locomotion: "slither", speak: "hsss"}

	var name, info string
	//infinite for loop
	for {
		fmt.Print("\nEnter name: ")
		_, _ = fmt.Scanf("%s", &name)
		fmt.Print("Enter information(food, locomotion, noise) needed :")
		_, _ = fmt.Scan(&info)

		name = strings.ToLower(name)
		info = strings.ToLower(info)
		//condition to get write record
		if val, ok := animals[name]; ok {
			switch {
			case info == "food":
				fmt.Printf("\nanimal = %s , food= %s\n", name, val.Eat())
			case info == "locomotion":
				fmt.Printf("\nanimal = %s , locomotion= %s\n", name, val.Move())
			case info == "noise":
				fmt.Printf("\nanimal = %s , noise= %s\n", name, val.Speak())
			default:
				fmt.Printf("\nanimal = %s , information ask is not available (food, locomotion, noise)\n", name)
			}
		} else {
			fmt.Println("Animal interred is not found in database")
		}
	}
}
