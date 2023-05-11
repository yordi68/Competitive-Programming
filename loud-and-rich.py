class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        n = len(richer)
        indegree = defaultdict(int)
        adjList = defaultdict(list)
        queue = deque()

        for rich, poor in richer:
            adjList[rich].append(poor)
            indegree[poor] += 1

        for i in range(len(quiet)):
            if indegree[i] == 0:
                queue.append(i)

        ans = list((range(len(quiet))))
        while queue:
            temp = queue.popleft()

            for neighbour in adjList[temp]:

                if quiet[ans[temp]] < quiet[ans[neighbour]]:
                    ans[neighbour] = ans[temp]

                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        return ans