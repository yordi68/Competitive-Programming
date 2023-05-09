class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for i in range(len(stones)):
            heapq.heappush(maxHeap, -stones[i])

        while len(maxHeap) > 1:
            largest = - (heapq.heappop(maxHeap))
            secondLargest = - (heapq.heappop(maxHeap))

            if largest != secondLargest:
                heapq.heappush(maxHeap, -(largest - secondLargest))

            
        return -maxHeap[0] if len(maxHeap) == 1 else 0