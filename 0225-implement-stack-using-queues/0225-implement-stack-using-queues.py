class MyStack:

    def __init__(self):
        self.stack = []
        self.q = []

    def push(self, x: int) -> None:
        while self.stack:
            self.q.append(self.stack.pop(0))
        self.stack.append(x)
        while self.q:
            self.stack.append(self.q.pop(0))

    def pop(self) -> int:
        return self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()