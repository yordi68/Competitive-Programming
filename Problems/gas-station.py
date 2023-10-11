class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx = -1
        curr = 0
        neg = 0
        for i in range(len(gas)):
            curr += gas[i] - cost[i]
            if curr < 0:
                neg += curr
                curr = 0
                idx = -1
            elif idx == -1 and curr >= 0:
                idx = i
        
        if curr >= abs(neg): 
            return idx
        else:
            return -1 