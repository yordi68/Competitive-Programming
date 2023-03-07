class StockSpanner:

    def __init__(self):
        self.monotonic_stack = []

    def next(self, price: int) -> int:
        count = 1
        while self.monotonic_stack and price >= self.monotonic_stack[-1][0]:
            popped = self.monotonic_stack.pop()
            count += popped[1]
        self.monotonic_stack.append([price,count])
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)