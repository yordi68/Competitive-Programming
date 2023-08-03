class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = []
        for pile in piles:
            heapq.heappush(maxHeap, -pile)

        while k:
            largest = - (heapq.heappop(maxHeap))
            remove = largest // 2
            add = largest - remove
            heapq.heappush(maxHeap, -add)

            k -= 1

        return - sum(maxHeap)