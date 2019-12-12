package main

// Drivaer function for link list
import "./LinkLists"

func main() {
	oneWayList := LinkLists.OneWayLinkList{}
	//oneWayList.Init() //initialise head with nill

	// Add new nodes

	oneWayList.InsertAtBeginning(3)
	oneWayList.InsertAtBeginning(2)
	oneWayList.InsertAtBeginning(1)

	oneWayList.PrintList()

	oneWayList.Append(4)
	oneWayList.Append(5)

	oneWayList.PrintList()

	oneWayList.InsertAtGivenPosition(8, 8)
	oneWayList.InsertAtGivenPosition(6, 6)
	oneWayList.InsertAtGivenPosition(7, 7)
	oneWayList.InsertAtGivenPosition(1, 0)
	oneWayList.InsertAtGivenPosition(0, 1)

	oneWayList.PrintList()

}
