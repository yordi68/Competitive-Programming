class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                heapq.heappush(maxHeap, -matrix[r][c])
                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)

        return - maxHeap[0]
