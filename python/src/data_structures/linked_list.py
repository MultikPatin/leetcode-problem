from typing import Self
from unittest.util import _MAX_LENGTH


class Node:
    def __init__(self, value: str, _next: Self | None) -> None:
        self._value = value
        self._next = _next

    def clear_next(self) -> None:
        self._next = None

    @property
    def value(self) -> str:
        return self._value

    @property
    def next(self) -> Self | None:
        return self._next

    @next.setter
    def next(self, value: Self | None) -> None:
        self._next = value


class LinkedList:
    _head: Node

    def __init__(self) -> None:
        self._length = 0

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Self:
        self._current = self._head
        return self

    def __next__(self) -> str:
        if self._current is None:
            raise StopIteration
        value = self._current.value
        self._current = self._current.next
        return value

    def __str__(self) -> str:
        result = []
        for i, v in enumerate(self):
            result.append(f"[{i}: {v}]")
        return " -> ".join(result)

    def get_node(self, index: int) -> Node | None:
        if index < 0 or index >= len(self):
            return None

        node = self._head
        for _ in range(index):
            if node is None:
                return None
            node = node.next
        return node

    def append(self, value: str) -> None:
        node = self.get_node(len(self) - 1)
        if node is None:
            self._head = Node(value, None)
        else:
            node.next = Node(value, None)
        self._length += 1

    def insert(self, index: int, value: str) -> None:
        if index < 0 or index > len(self):
            return

        if index == 0:
            self._head = Node(value, self._head)
        else:
            node = self.get_node(index - 1)
            if node is not None:
                node.next = Node(value, node.next)
        self._length += 1

    def remove(self, index: int) -> None:
        if index < 0 or index >= len(self):
            return

        if index == 0:
            if self._head is not None:
                self._head = self._head.next
        else:
            node = self.get_node(index - 1)
            if node is not None:
                next_node = node.next
                if next_node is not None:
                    node.next = next_node.next
        self._length -= 1


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append("first")
    linked_list.append("second")
    linked_list.append("third")
    print(linked_list)

    linked_list.insert(1, "1node")
    print(linked_list)

    linked_list.remove(1)
    print(linked_list)

    linked_list.insert(3, "3node")
    print(linked_list)

    linked_list.remove(3)
    print(linked_list)

    linked_list.insert(4, "4node")
    print(linked_list)

    linked_list.remove(4)
    print(linked_list)
