class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        adjList = defaultdict(list)
        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if isConnected[r][c] == 1:
                    adjList[r + 1].append(c + 1)


        visited = set()
        def dfs(adjList, key):
            visited.add(key)
            for value in adjList[key]:
                if value not in visited:
                    dfs(adjList, value)


        cnt = 0
        for key in adjList.keys():
            if key not in visited:
                dfs(adjList, key)
                cnt += 1

                


        return cnt