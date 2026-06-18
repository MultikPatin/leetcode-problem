package main

import (
	"errors"
	"fmt"
)

var (
	ErrInvalidNodeIndex    = errors.New("node index invalid")
	ErrDeleteFromEmptyList = errors.New("can delete from empty list")
)

type Node struct {
	value string
	next  *Node
}

func NewNode(value string) *Node {
	return &Node{
		value: value,
	}
}

type LinkedList struct {
	head   *Node
	length int
}

func NewLinkedList() *LinkedList {
	return &LinkedList{}
}

func (l *LinkedList) isIndexValid(index int) bool {
	return index >= 0 && index < l.length
}

func (l *LinkedList) incrementLength() {
	l.length++
}

func (l *LinkedList) decrementLength() {
	l.length--
}

func (l *LinkedList) Empty() bool {
	return l.length == 0
}

func (l *LinkedList) Length() int {
	return l.length
}

func (l *LinkedList) Print() {
	node := l.head
	for node != nil {
		fmt.Printf("%s -> ", node.value)
		node = node.next
	}
	fmt.Println("None")
}

func (l *LinkedList) Tail() *Node {
	node := l.head
	index := l.length - 1
	for index > 0 {
		node = node.next
		index--
	}
	return node
}

func (l *LinkedList) GetNode(index int) (*Node, error) {
	if !l.isIndexValid(index) {
		return nil, ErrInvalidNodeIndex
	}

	if index == 0 {
		return l.head, nil
	}
	node := l.head
	for index > 0 {
		node = node.next
		index--
	}
	return node, nil
}

func (l *LinkedList) Append(node *Node) {
	if l.Empty() {
		l.head = node
	} else {
		tail := l.Tail()
		tail.next = node
	}
	l.incrementLength()
}

func (l *LinkedList) Insert(index int, node *Node) error {
	if !l.isIndexValid(index) {
		return ErrInvalidNodeIndex
	}

	if index == 0 {
		node.next = l.head
		l.head = node
		l.incrementLength()
		return nil
	}
	previousNode, err := l.GetNode(index - 1)
	if err != nil {
		return err
	}
	node.next = previousNode.next
	previousNode.next = node
	l.incrementLength()
	return nil
}

func (l *LinkedList) Delete(index int) error {
	previousNode, err := l.GetNode(index - 1)
	if err != nil {
		return err
	}
	previousNode.next = previousNode.next.next
	l.decrementLength()
	return nil
}

func (l *LinkedList) DeleteHead() error {
	if l.Empty() {
		return ErrDeleteFromEmptyList
	}
	l.head = l.head.next
	l.decrementLength()
	return nil

}

func (l *LinkedList) DeleteTail() error {
	if l.Empty() {
		return ErrDeleteFromEmptyList
	}
	err := l.Delete(l.length - 1)
	if err != nil {
		return err
	}
	return nil
}

func main() {
	linkedList := NewLinkedList()
	n4 := NewNode("forth")
	n3 := NewNode("third")
	n2 := NewNode("second")
	n1 := NewNode("first")

	err := linkedList.DeleteHead()
	if err != nil {
		fmt.Println(err)
	}

	linkedList.Append(n1)
	linkedList.Append(n3)
	linkedList.Append(n4)
	linkedList.Append(n2)

	linkedList.Print()
	fmt.Println(linkedList.Length())

	err = linkedList.Delete(5)
	if err != nil {
		fmt.Println(err)
	}
	err = linkedList.Delete(2)
	if err != nil {
		fmt.Println(err)
	}
	linkedList.Print()
	err = linkedList.DeleteHead()
	if err != nil {
		fmt.Println(err)
	}
	linkedList.Print()
	fmt.Println(linkedList.Length())
	err = linkedList.DeleteTail()
	if err != nil {
		fmt.Println(err)
	}

	linkedList.Print()
	fmt.Println(linkedList.Length())

	m4 := NewNode("m_forth")
	m3 := NewNode("m_third")
	m2 := NewNode("m_second")
	m1 := NewNode("m_first")

	linkedList.Append(m1)
	linkedList.Append(m4)

	linkedList.Print()
	fmt.Println(linkedList.Length())

	err = linkedList.Insert(0, m3)
	if err != nil {
		fmt.Println(err)
	}

	linkedList.Print()
	fmt.Println(linkedList.Length())

	err = linkedList.Insert(4, m2)
	if err != nil {
		fmt.Println(err)
	}

	err = linkedList.Insert(2, m2)
	if err != nil {
		fmt.Println(err)
	}

	linkedList.Print()
	fmt.Println(linkedList.Length())

}
