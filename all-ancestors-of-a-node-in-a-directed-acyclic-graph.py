class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        adjList = defaultdict(list)
        dependency = defaultdict(int)
        queue = deque()
        ancestor = [set() for _ in range(n)]

        for fr, to in edges:
            adjList[fr].append(to)
            dependency[to] += 1

        for node in range(n):
            if dependency[node] == 0:
                queue.append(node)
        
        while queue:
            temp = queue.popleft()

            for neighbour in adjList[temp]:
                ancestor[neighbour].add(temp)
                ancestor[neighbour].update(ancestor[temp])

                dependency[neighbour] -= 1

                if dependency[neighbour] == 0:
                    queue.append(neighbour)

        for i in range(len(ancestor)):
            ancestor[i] = sorted(list(ancestor[i]))

        return ancestor