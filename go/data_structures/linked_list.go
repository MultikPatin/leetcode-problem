package main

import "fmt"

type Node struct {
	value string
	next  *Node
}

func getNodeByIndex(node *Node, index int) *Node {
	for index > 0 {
		node = node.next
		index--
	}
	return node
}

func insertNode(head *Node, index int, value string) *Node {
	newNode := &Node{value: value}
	if index == 0 {
		newNode.next = head
		return newNode
	}
	previousNode := getNodeByIndex(head, index-1)
	newNode.next = previousNode.next
	previousNode.next = newNode
	return head
}

func deleteNode(head *Node, index int) *Node {
	if index == 0 {
		return head.next
	}
	previousNode := getNodeByIndex(head, index-1)
	previousNode.next = previousNode.next.next
	return head
}

func printLinkedList(vertex *Node) {
	for vertex != nil {
		fmt.Printf("%s -> ", vertex.value)
		vertex = vertex.next
	}
	fmt.Println("None")
}

func main() {
	n3 := &Node{value: "third"}
	n2 := &Node{value: "second", next: n3}
	n1 := &Node{value: "first", next: n2}
	printLinkedList(n1)
	printLinkedList(n2)

	node, index, value := n1, 2, "new_node"
	head := insertNode(node, index, value)
	printLinkedList(head)

	node, index = head, 1
	head = deleteNode(node, index)
	printLinkedList(head)

}
