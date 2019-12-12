package main

import "fmt"

/* Go does not have classes so we need to use struct instead,
   We can associate a methods with structures
*/

const totalMarks  float64 = 500
type student struct{
	name string
	marks [5]float64
}

func main(){
	std1 := student{name: "sudhanshu",
		            marks: [5]float64{60,55,70,83,94}} // how to initialise value to go array

	fmt.Println("percentage  marks of ",std1.name,"is ",std1.averageMarks())
}

// this function is binded to student structure
func (s student) averageMarks() float32{
	var myTotalMarks float64 = 0
	for  index := range s.marks{
		myTotalMarks = myTotalMarks + s.marks[index]
	}
	return float32((myTotalMarks/totalMarks)* float64(100)) //typecast float64 to float32
}
