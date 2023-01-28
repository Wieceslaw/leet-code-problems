class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

    def throw(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

    def pop(self) -> int:
        if not self.stack2:
            self.throw()
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            self.throw()
        return self.stack2[-1]
