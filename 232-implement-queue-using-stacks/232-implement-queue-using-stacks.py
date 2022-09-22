class MyQueue:

    def __init__(self):
        self.q = []
        self.p = []

    def push(self, x: int) -> None:
        while self.q:
            self.p.append(self.q.pop())
        self.q.append(x)
        while self.p:
            self.q.append(self.p.pop())

    def pop(self) -> int:
        return self.q.pop()

    def peek(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()