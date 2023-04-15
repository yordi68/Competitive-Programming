class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adjList = defaultdict(set)
        visited = set()

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    x,y,r = bombs[i]
                    a,b,c = bombs[j]
                    distance  = sqrt(pow(x - a,2) + pow(y - b, 2))
                    if r >= distance:
                        adjList[i].add(j)

        def dfs(node):

            visited.add(node)
            boom = 0
            for value in adjList[node]:
                if value not in visited:
                    boom += dfs(value)
            return boom + 1

        maxBoom = 1
        s = list(adjList.keys())
        for key in s:   
            maxBoom = max(maxBoom,dfs(key))
            visited = set()

        return maxBoom