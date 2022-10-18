class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passChange = [0] * 1001
        currPass = 0
        for t in trips:
            numPass,start,end = t
            passChange[start] += numPass
            passChange[end] -= numPass
        for i in range(1001):
            currPass += passChange[i]
            if currPass > capacity:
                return False
        return True