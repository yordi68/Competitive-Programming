class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.deq = deque()
        self.hashmap = defaultdict(int)

    def consec(self, num: int) -> bool:
        self.deq.append(num)
        self.hashmap[num] += 1
        
        if len(self.deq) > self.k:
            self.hashmap[self.deq[0]] -= 1
            
            if self.hashmap[self.deq[0]] == 0:
                del self.hashmap[self.deq[0]] 
                
            self.deq.popleft()
                
        if self.hashmap[self.value] == self.k:
            return True
        
        return False
            
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)