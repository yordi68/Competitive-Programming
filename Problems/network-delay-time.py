class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for x, y, z in times:
            graph[x - 1].append((y - 1,z))
        
        distances = [float("inf") for i in range(n)]
        distances[k - 1] = 0
        visited = set()

        heap = [(0, k - 1)]

        while heap:
            curr, node = heapq.heappop(heap)
            if node in visited:
                continue

            visited.add(node)
            for neigh, weigh in graph[node]:
                dist = weigh + curr
                if dist < distances[neigh]:
                    distances[neigh] = dist
                    heapq.heappush(heap, (dist, neigh))
        print(distances)    
        ans = max(distances)
        return ans if ans != float("inf") else -1
