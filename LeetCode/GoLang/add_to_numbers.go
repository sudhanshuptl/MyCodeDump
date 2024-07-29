package main

import (
	"fmt"
)

// https://leetcode.com/problems/add-two-numbers/

// ListNode represents a node in a singly linked list
type ListNode struct {
	Val  int
	Next *ListNode
}

// addTwoNumbers adds two numbers represented by linked lists
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	// Dummy head node to simplify edge cases handling
	dummyHead := &ListNode{}
	// Current node to build the resulting linked list
	current := dummyHead
	// Carry to store the carry-over value in addition
	carry := 0

	// Iterate through both linked lists until both are exhausted
	for l1 != nil || l2 != nil {
		// Extract the values from the current nodes of l1 and l2 (0 if nil)
		x, y := 0, 0
		if l1 != nil {
			x = l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			y = l2.Val
			l2 = l2.Next
		}

		// Calculate the sum of the current digits and the carry
		sum := carry + x + y
		// Update the carry for the next iteration
		carry = sum / 10
		// Create a new node for the result list with the value sum % 10
		current.Next = &ListNode{Val: sum % 10}
		// Move to the next node in the result list
		current = current.Next
	}

	// If there's any carry left, add a new node with the carry value
	if carry > 0 {
		current.Next = &ListNode{Val: carry}
	}

	// Return the next node of dummyHead which is the actual head of the result list
	return dummyHead.Next
}

// printList prints all the values in the linked list
func printList(node *ListNode) {
	for node != nil {
		fmt.Printf("%d ", node.Val)
		node = node.Next
	}
	fmt.Println()
}

// func main() {
// 	// Example 1
// 	l1 := &ListNode{Val: 2, Next: &ListNode{Val: 4, Next: &ListNode{Val: 3}}}
// 	l2 := &ListNode{Val: 5, Next: &ListNode{Val: 6, Next: &ListNode{Val: 4}}}
// 	result := addTwoNumbers(l1, l2)
// 	fmt.Print("Example 1: ")
// 	printList(result) // Output: 7 0 8

// 	// Example 2
// 	l1 = &ListNode{Val: 0}
// 	l2 = &ListNode{Val: 0}
// 	result = addTwoNumbers(l1, l2)
// 	fmt.Print("Example 2: ")
// 	printList(result) // Output: 0

// 	// Example 3
// 	l1 = &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9}}}}}}}
// 	l2 = &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9}}}}
// 	result = addTwoNumbers(l1, l2)
// 	fmt.Print("Example 3: ")
// 	printList(result) // Output: 8 9 9 9 0 0 0 1
// }
