package Nodes

// Defining Code infrastructure of link list


//type Node interface {
//	getData() int
//	getNext() *Node
//	createNode(int) Node
//}

type OneWayNode struct {
	Data int
	Next *OneWayNode
}

//func (node OneWayNode)getData() int{
//	return node.Data
//}
//
//func (node OneWayNode)getNext() *OneWayNode{
//	return node.Next
//}