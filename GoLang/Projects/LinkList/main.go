package main

import "./LinkLists"

func main(){
	oneWayList := LinkLists.OneWayLinkList{}
	//oneWayList.Init() //initialise head with nill

	// Add new nodes

	oneWayList.InsertAtBeginning(3)
	oneWayList.InsertAtBeginning(2)
	oneWayList.InsertAtBeginning(1)

	oneWayList.PrintList()

	oneWayList.Append( 4)
	oneWayList.Append(5)

	oneWayList.PrintList()

}
