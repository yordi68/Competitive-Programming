class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for x, y, z in flights:
            graph[x].append((y, z))

        k -= 1
        queue = deque()
        queue.append((src, 0, 0))
        visited = [-1] * n
        visited[src] = 0

        while queue:
            curr, price, count = queue.popleft()
            if count - 1 > k:
                 continue
            for node, money in graph[curr]:
                if visited[node] == -1:
                    queue.append((node, price + money, count + 1))
                    visited[node] = (price + money)
  
                else:
                    if visited[node] > (price + money):
                        visited[node] = (price + money)
                        queue.append((node, price + money, count + 1))
        return visited[dst]