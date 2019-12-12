package main

// Using interface to provide command datatype as input to function
import "fmt"

type Dimention2D interface {
	Area() float32
	Perimeter() float32
}
type Traingle struct {
	base   float32
	height float32
}

type Rectangle struct {
	length float32
	width  float32
}

func (td Traingle) Area() float32 {
	return 0.5 * td.base * td.height
}

func (td Traingle) Perimeter() float32 {
	return td.base + (td.height)*0.25
}

func (rt Rectangle) Area() float32 {
	return rt.length * rt.width
}

func (rt Rectangle) Perimeter() float32 {
	return (rt.length + rt.width) * 2
}

//this function can handle both datatype
func summry2d(fig Dimention2D) {
	fmt.Println("area: ", fig.Area(), "  perimeter: ", fig.Perimeter())
}

func summry2dAssert(fig Dimention2D) {
	rectangle, ok := fig.(Rectangle)
	if ok {
		fmt.Println("Rectangle area: ", rectangle.Area(), " Rectangle perimeter: ", rectangle.Perimeter())
	}
	tri, ok := fig.(Traingle)
	if ok {
		fmt.Println("Traingle area: ", tri.Area(), " Triangle perimeter: ", tri.Perimeter())
	}
}

func summry2dTypeSwitch(fig Dimention2D) {

	switch fig.(type) {
	case Rectangle:
		fmt.Println("Rectangle area: ", fig.Area(), " Rectangle perimeter: ", fig.Perimeter())
	case Traingle:
		fmt.Println("Traingle area: ", fig.Area(), " Triangle perimeter: ", fig.Perimeter())
	default:
		fmt.Println("Rules not defined")
	}
}

func main() {
	var td Traingle = Traingle{34, 54}
	var rt Rectangle = Rectangle{50, 100}

	fmt.Println("Traingale")
	summry2d(td)
	fmt.Println("Rectangle")
	summry2d(rt)
	fmt.Println("using type assertion---------------------")
	summry2dAssert(td)
	summry2dAssert(rt)

	fmt.Println("using type switch---------------------")
	summry2dTypeSwitch(td)
	summry2dTypeSwitch(rt)
}
