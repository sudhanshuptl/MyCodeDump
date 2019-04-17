package Introduction_to_go

import "fmt"

func main() {
	// key value pair
	// map are implementation of hash table in golang
	// then use make to actually create that hashmap

	var idMap map[string]int
	idMap = make(map[string]int)

	idMap["age"] = 100

	fmt.Println("Hashmap : ", idMap)

	map2 := map[string]int{"Jan": 1, "Feb": 2, "Mar": 8}

	fmt.Println("new map: ", map2)

	delete(map2, "Mar")
	fmt.Println("after deleting march : ", map2)

	// first value be value associated with key second response will be if key is available or not so boolean
	val, isPresent := map2["Jan"]
	fmt.Println("is key is available in map : ", isPresent, "value :", val)

	//iterate over map
	for key, val := range map2 {
		fmt.Printf(" %s : %d \n", key, val)
	}

}
