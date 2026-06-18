package linked_list

import (
	"errors"
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

func (l *LinkedList) incLength() {
	l.length++
}

func (l *LinkedList) decLength() {
	l.length--
}

func (l *LinkedList) IsEmpty() bool {
	return l.length == 0
}

func (l *LinkedList) Length() int {
	return l.length
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

func (l *LinkedList) Get(index int) (*Node, error) {
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
	if l.IsEmpty() {
		l.head = node
	} else {
		tail := l.Tail()
		tail.next = node
	}
	l.incLength()
}

func (l *LinkedList) Insert(index int, node *Node) error {
	if index == 0 {
		node.next = l.head
		l.head = node
		l.incLength()
		return nil
	}
	previousNode, err := l.Get(index - 1)
	if err != nil {
		return err
	}
	node.next = previousNode.next
	previousNode.next = node
	l.incLength()
	return nil
}

func (l *LinkedList) Delete(index int) error {
	previousNode, err := l.Get(index - 1)
	if err != nil {
		return err
	}
	previousNode.next = previousNode.next.next
	l.decLength()
	return nil
}

func (l *LinkedList) DeleteHead() error {
	if l.IsEmpty() {
		return ErrDeleteFromEmptyList
	}
	l.head = l.head.next
	l.decLength()
	return nil

}

func (l *LinkedList) DeleteTail() error {
	if l.IsEmpty() {
		return ErrDeleteFromEmptyList
	}
	err := l.Delete(l.length - 1)
	if err != nil {
		return err
	}
	return nil
}
