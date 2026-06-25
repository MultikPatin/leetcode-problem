class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.empty():
            el = self.stack[0]
            self.stack = self.stack[1:]
            return el
        return 0

    def peek(self) -> int:
        if not self.empty():
            return self.stack[0]
        return 0

    def empty(self) -> bool:
        return len(self.stack) == 0
