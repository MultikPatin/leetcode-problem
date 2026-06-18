package linked_list

import (
	"errors"
	"testing"
)

func TestNewNode(t *testing.T) {
	node := NewNode("test")

	if node.value != "test" {
		t.Errorf("expected value 'test', got '%s'", node.value)
	}

	if node.next != nil {
		t.Errorf("expected next to be nil, got %v", node.next)
	}
}

func TestNewLinkedList(t *testing.T) {
	list := NewLinkedList()

	if list.head != nil {
		t.Errorf("expected head to be nil, got %v", list.head)
	}

	if list.length != 0 {
		t.Errorf("expected length 0, got %d", list.length)
	}
}

func TestIsIndexValid(t *testing.T) {
	list := NewLinkedList()
	list.incLength() // length = 1

	tests := []struct {
		name     string
		index    int
		expected bool
	}{
		{"negative index", -1, false},
		{"zero index with length 1", 0, true},
		{"valid index with length 1", 0, true},
		{"out of range", 1, false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := list.isIndexValid(tt.index)
			if result != tt.expected {
				t.Errorf("isIndexValid(%d) = %v, expected %v", tt.index, result, tt.expected)
			}
		})
	}
}

func TestIncLength(t *testing.T) {
	list := NewLinkedList()
	list.incLength()

	if list.length != 1 {
		t.Errorf("expected length 1, got %d", list.length)
	}

	list.incLength()
	list.incLength()

	if list.length != 3 {
		t.Errorf("expected length 3, got %d", list.length)
	}
}

func TestDecLength(t *testing.T) {
	list := NewLinkedList()
	list.length = 5
	list.decLength()

	if list.length != 4 {
		t.Errorf("expected length 4, got %d", list.length)
	}

	list.decLength()
	list.decLength()

	if list.length != 2 {
		t.Errorf("expected length 2, got %d", list.length)
	}
}

func TestIsEmpty(t *testing.T) {
	list := NewLinkedList()

	if !list.IsEmpty() {
		t.Errorf("expected empty list, but list is not empty")
	}

	list.incLength()

	if list.IsEmpty() {
		t.Errorf("expected non-empty list, but list is empty")
	}
}

func TestLength(t *testing.T) {
	list := NewLinkedList()

	if list.Length() != 0 {
		t.Errorf("expected length 0, got %d", list.Length())
	}

	list.incLength()
	list.incLength()
	list.incLength()

	if list.Length() != 3 {
		t.Errorf("expected length 3, got %d", list.Length())
	}
}

func TestGet(t *testing.T) {
	list := NewLinkedList()

	t.Run("get from empty list", func(t *testing.T) {
		_, err := list.Get(0)
		if !errors.Is(err, ErrInvalidNodeIndex) {
			t.Errorf("expected ErrInvalidNodeIndex, got %v", err)
		}
	})

	list.Append(NewNode("first"))
	list.Append(NewNode("second"))
	list.Append(NewNode("third"))

	tests := []struct {
		name     string
		index    int
		expected string
		err      error
	}{
		{"negative index", -1, "", ErrInvalidNodeIndex},
		{"out of range index", 3, "", ErrInvalidNodeIndex},
		{"first element", 0, "first", nil},
		{"middle element", 1, "second", nil},
		{"last element", 2, "third", nil},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			node, err := list.Get(tt.index)
			if !errors.Is(err, tt.err) {
				t.Errorf("expected error %v, got %v", tt.err, err)
			}
			if err == nil && node.value != tt.expected {
				t.Errorf("expected value '%s', got '%s'", tt.expected, node.value)
			}
		})
	}
}

func TestAppend(t *testing.T) {
	list := NewLinkedList()

	node1 := NewNode("first")
	list.Append(node1)

	if list.head != node1 {
		t.Errorf("expected head to be node1, got %v", list.head)
	}

	if list.length != 1 {
		t.Errorf("expected length 1, got %d", list.length)
	}

	node2 := NewNode("second")
	list.Append(node2)

	if list.head.next != node2 {
		t.Errorf("expected head.next to be node2, got %v", list.head.next)
	}

	if list.length != 2 {
		t.Errorf("expected length 2, got %d", list.length)
	}

	node3 := NewNode("third")
	list.Append(node3)

	tail := list.Tail()
	if tail != node3 {
		t.Errorf("expected tail to be node3, got %v", tail)
	}
}

func TestInsert(t *testing.T) {
	list := NewLinkedList()

	t.Run("insert to empty list at index 0", func(t *testing.T) {
		node := NewNode("first")
		err := list.Insert(0, node)

		if err != nil {
			t.Errorf("unexpected error: %v", err)
		}

		if list.head != node {
			t.Errorf("expected head to be node, got %v", list.head)
		}

		if list.length != 1 {
			t.Errorf("expected length 1, got %d", list.length)
		}
	})

	list.Append(NewNode("second"))
	list.Append(NewNode("third"))

	t.Run("insert at beginning", func(t *testing.T) {
		node := NewNode("new_first")
		err := list.Insert(0, node)

		if err != nil {
			t.Errorf("unexpected error: %v", err)
		}

		if list.head != node {
			t.Errorf("expected head to be node, got %v", list.head)
		}

		if list.head.next != nil && list.head.next.value != "first" {
			t.Errorf("expected second element to be 'first', got '%s'", list.head.next.value)
		}

		if list.length != 4 {
			t.Errorf("expected length 4, got %d", list.length)
		}
	})

	t.Run("insert in middle", func(t *testing.T) {
		node := NewNode("between")
		err := list.Insert(2, node)

		if err != nil {
			t.Errorf("unexpected error: %v", err)
		}

		secondNode, _ := list.Get(1)
		if secondNode.next != node {
			t.Errorf("expected secondNode.next to be node, got %v", secondNode.next)
		}

		if list.length != 5 {
			t.Errorf("expected length 5, got %d", list.length)
		}
	})

	t.Run("insert at end", func(t *testing.T) {
		node := NewNode("last")
		err := list.Insert(list.length, node)

		if err != nil {
			t.Errorf("unexpected error: %v", err)
		}

		tail := list.Tail()
		if tail != node {
			t.Errorf("expected tail to be node, got %v", tail)
		}
	})

	t.Run("insert at invalid index", func(t *testing.T) {
		node := NewNode("invalid")
		err := list.Insert(100, node)

		if !errors.Is(err, ErrInvalidNodeIndex) {
			t.Errorf("expected ErrInvalidNodeIndex, got %v", err)
		}
	})
}

func TestDelete(t *testing.T) {
	list := NewLinkedList()
	list.Append(NewNode("first"))
	list.Append(NewNode("second"))
	list.Append(NewNode("third"))

	t.Run("delete from empty list", func(t *testing.T) {
		emptyList := NewLinkedList()
		err := emptyList.Delete(0)
		if !errors.Is(err, ErrInvalidNodeIndex) {
			t.Errorf("expected ErrInvalidNodeIndex, got %v", err)
		}
	})

	t.Run("delete middle element", func(t *testing.T) {
		err := list.Delete(1)

		if err != nil {
			t.Errorf("unexpected error: %v", err)
		}

		if list.length != 2 {
			t.Errorf("expected length 2, got %d", list.length)
		}

		firstNode, _ := list.Get(0)
		if firstNode.next.value != "third" {
			t.Errorf("expected second element to be 'third', got '%s'", firstNode.next.value)
		}
	})

	t.Run("delete last element", func(t *testing.T) {
		err := list.Delete(1)

		if err != nil {
			t.Errorf("unexpected error: %v", err)
		}

		if list.length != 1 {
			t.Errorf("expected length 1, got %d", list.length)
		}
	})

	t.Run("delete at invalid index", func(t *testing.T) {
		err := list.Delete(100)

		if !errors.Is(err, ErrInvalidNodeIndex) {
			t.Errorf("expected ErrInvalidNodeIndex, got %v", err)
		}
	})
}

func TestDeleteHead(t *testing.T) {
	list := NewLinkedList()

	t.Run("delete from empty list", func(t *testing.T) {
		err := list.DeleteHead()
		if !errors.Is(err, ErrDeleteFromEmptyList) {
			t.Errorf("expected ErrDeleteFromEmptyList, got %v", err)
		}
	})

	list.Append(NewNode("first"))
	list.Append(NewNode("second"))
	list.Append(NewNode("third"))

	originalHead := list.head

	t.Run("delete head", func(t *testing.T) {
		err := list.DeleteHead()

		if err != nil {
			t.Errorf("unexpected error: %v", err)
		}

		if list.head == originalHead {
			t.Errorf("expected head to be changed")
		}

		if list.head.value != "second" {
			t.Errorf("expected new head value to be 'second', got '%s'", list.head.value)
		}

		if list.length != 2 {
			t.Errorf("expected length 2, got %d", list.length)
		}
	})
}

func TestDeleteTail(t *testing.T) {
	list := NewLinkedList()

	t.Run("delete from empty list", func(t *testing.T) {
		err := list.DeleteTail()
		if !errors.Is(err, ErrDeleteFromEmptyList) {
			t.Errorf("expected ErrDeleteFromEmptyList, got %v", err)
		}
	})

	list.Append(NewNode("first"))
	list.Append(NewNode("second"))
	list.Append(NewNode("third"))

	t.Run("delete tail", func(t *testing.T) {
		err := list.DeleteTail()

		if err != nil {
			t.Errorf("unexpected error: %v", err)
		}

		if list.length != 2 {
			t.Errorf("expected length 2, got %d", list.length)
		}

		tail := list.Tail()
		if tail.value != "second" {
			t.Errorf("expected new tail value to be 'second', got '%s'", tail.value)
		}
	})
}

func TestTail(t *testing.T) {
	list := NewLinkedList()

	t.Run("tail from empty list", func(t *testing.T) {
		tail := list.Tail()
		if tail != nil {
			t.Errorf("expected nil tail, got %v", tail)
		}
	})

	list.Append(NewNode("first"))

	t.Run("tail from single element list", func(t *testing.T) {
		tail := list.Tail()
		if tail.value != "first" {
			t.Errorf("expected tail value 'first', got '%s'", tail.value)
		}
	})

	list.Append(NewNode("second"))
	list.Append(NewNode("third"))

	t.Run("tail from multiple elements list", func(t *testing.T) {
		tail := list.Tail()
		if tail.value != "third" {
			t.Errorf("expected tail value 'third', got '%s'", tail.value)
		}
	})
}
