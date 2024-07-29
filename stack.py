from typing import Any


class Stack:

    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def __repr__(self):
        return str(self.stack)

    def is_empty(self) -> bool:
        return self.stack == []

    def push(self, value: Any) -> None:
        self.stack.append(value)

    def pop(self) -> Any:
        return self.stack.pop()

    def peek(self) -> Any:
        return self.stack[-1]

    def size(self) -> int:
        return len(self.stack)


