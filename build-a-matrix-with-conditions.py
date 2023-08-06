class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        ans = [[0] * k for _ in range(k)]

        def getOrder(edges):
            adjList = defaultdict(list)
            indegree = [0] * k

            for a, b in edges:
                adjList[a].append(b)
                indegree[b - 1] += 1
            queue = deque()
            for i in range(len(indegree)):
                if indegree[i] == 0:
                    queue.append(i + 1)
            order = []
            while queue:
                curr = queue.popleft()
                order.append(curr)
                for neighbour in adjList[curr]:
                    indegree[neighbour - 1] -= 1
                    if indegree[neighbour - 1] == 0:
                        queue.append(neighbour)
            return order

        rowOrder = getOrder(rowConditions)
        colOrder = getOrder(colConditions)

        if len(rowOrder) != k or len(colOrder) != k:
            return []

        for row in range(len(rowOrder)):
            col = colOrder.index(rowOrder[row])
            ans[row][col] = rowOrder[row]

        return ans