class Stack[T]:
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def peek(self) -> T:
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)


if __name__ == "__main__":
    stack = Stack[str]()
    stack.push("apple")
    stack.push("banana")
    stack.push("orange")
    stack.pop()
