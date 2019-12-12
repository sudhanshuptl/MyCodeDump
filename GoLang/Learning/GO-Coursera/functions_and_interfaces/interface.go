package main

import "fmt"

type noise interface {
	Speak() string
}

type Dog struct {
	name  string
	sound string
}

//automatically link to interface and override
func (dg Dog) Speak() string {
	return dg.sound
}

type Bird struct {
	name string
}

//automatically link to interface and override
func (bd Bird) Speak() string {
	return "chi - chi"
}

func main() {
	var dog Dog = Dog{name: "Tomy", sound: "Bark"}
	var bird Bird = Bird{"hanna"}
	fmt.Println("name : ", dog.name, " speak :", dog.Speak())
	fmt.Println("name : ", bird.name, " speak :", bird.Speak())

	//Interface values
	// can be treated like any other values, assign to variable passed,return
	// it has two components
	// Dynamic type :concrete type which it is assign to
	//Dynamic values : values of dynamic type
	var n1 noise
	// dynanmic interface type
	n1 = dog
	fmt.Println(n1.Speak()) // values in dog is used in speak function

	//interface with nill dynamic value
	var s1 noise
	var b1 *Bird
	//s1 has dynamic type of dog but does not have any value as d1 is pointer to dog but not have actual dog so has no value
	s1 = b1
	fmt.Println(s1.Speak()) //it will fail but we can make call even without dynamic value
	// without dynanic type it is impossible to know which method it referred to

}

/*
Way to use interfaces
1:	Need a function that take multiple type of parameter
	function foo parameter is Type x and Type y
    then define interface Z then foo take Z as parameter
	Type x, y will satisfy Z
*/

/*
 Empty interface specify no methods So all type satisfy empty interface
ex
func PrintMe(val interface{}){
	fmt.Println(val)
}
it will accesp and print any value

*/
