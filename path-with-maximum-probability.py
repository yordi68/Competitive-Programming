class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        distances = [float("inf") for _ in range(n)]
        graph = defaultdict(list)
        for i, arr in enumerate(edges):
            From, To = arr
            graph[From].append((To, -1 * succProb[i]))
            graph[To].append((From, -1 * succProb[i]))
        
        heap = [(start_node, 1)]
        visited = set()

        while heap:
            curr, dist = heapq.heappop(heap)

            if curr in visited: continue

            for neigh, weigh in graph[curr]:
                distance = dist * weigh

                if distance > 0:
                    distance = -1 * distance

                if distance < distances[neigh]:
                    distances[neigh] = distance
                    heapq.heappush(heap, (neigh, distance))
        return -1 * distances[end_node] if distances[end_node] != float("inf") else 0