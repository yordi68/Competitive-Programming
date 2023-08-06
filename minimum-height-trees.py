class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if edges == []:
            return [0]

        adjList = defaultdict(list)
        indegree = defaultdict(int)
        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
            indegree[x] += 1
            indegree[y] += 1

        queue = deque([])
        visited = set()
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
                visited.add(i)
    
        ans = []
        while queue:
            ans = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                ans.append(curr)
                for child in adjList[curr]:
                    indegree[child] -= 1
                    if indegree[child] == 1 and child not in visited:
                        queue.append(child)
                        visited.add(child)
        return ans