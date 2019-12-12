package LinkLists

// Data structure and functionality of one way link list

import (
	"../Nodes"
	"fmt"
)

type OneWayLinkList struct {
	head *Nodes.OneWayNode
}

func (list *OneWayLinkList) InsertAtBeginning(data int){
	//Node : If We dont use list pointer then changes won't resides over multiple call as pass by value
	// better example of that case is PrintList
	newNode := Nodes.OneWayNode{Data: data, Next:nil}

	//insert at beginning
	if list.head == nil{
		//Insert First Element
		list.head = &newNode
	} else {
		newNode.Next = list.head
		list.head = &newNode
	}

	defer fmt.Println("New Node inserted at beginning with data : ", list.head.Data)

}

func (list *OneWayLinkList) Append(data int){
	//Insert at the END
	var ptr *Nodes.OneWayNode

	if list.head == nil{
		list.InsertAtBeginning(data)
	}

	newNode := Nodes.OneWayNode{Data: data, Next:nil}
	ptr = list.head
	// Move till the last Node
	for {
		if ptr.Next == nil{
			break
		} else{
			ptr = ptr.Next
		}
	}
	ptr.Next = &newNode
	defer fmt.Println("New Node inserted at End with data : ", ptr.Next.Data)
}

func (list OneWayLinkList)PrintList(){
	//Printing One Way link list
	//Any change in using ptr is reside withing this function and won't impact source as we are using pass by value
	var ptr *Nodes.OneWayNode

	ptr = list.head
	fmt.Print("Head")
	for{
		if ptr == nil{
			fmt.Print(" -> NULL\n")
			break
		}
		fmt.Printf(" -> %d", ptr.Data)
		ptr = ptr.Next
	}

}




