class MyStack:
    def __init__(self):
        self.array = []

    def push(self, x: int) -> None:
        self.array.append(x)

    def pop(self) -> int:
        if len(self.array):
            return self.array.pop()
        return None

    def top(self) -> int:
        if len(self.array):
            return self.array[-1]
        return None

    def empty(self) -> bool:
        return not len(self.array)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
