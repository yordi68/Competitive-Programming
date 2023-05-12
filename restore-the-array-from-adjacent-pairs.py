class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()
        positions = defaultdict(int)
        answer = ['empty' for i in range(len(adjacentPairs) + 1)]
        visited = set()

        def inBound(index):
            return 0 <= index <= len(adjacentPairs)

        for From, To in adjacentPairs:
            graph[From].append(To)
            graph[To].append(From)
            indegree[From] += 1
            indegree[To] += 1

        for num in indegree.keys():
            if indegree[num] == 1:
                visited.add(num)
                queue.append(num)

        positions[queue[0]] = 0
        positions[queue[1]] = len(adjacentPairs)
        answer[0] = queue[0]
        answer[len(adjacentPairs)] = queue[1]
        print(answer)
        while queue:
            currNode = queue.popleft()
            
            for neighbour in graph[currNode]:
                if neighbour not in visited:
                    if inBound(positions[currNode] + 1) and answer[positions[currNode] + 1] == 'empty':
                        positions[neighbour] = (positions[currNode] + 1)
                        answer[positions[neighbour]] = neighbour

                    else:
                        positions[neighbour] = (positions[currNode] - 1)
                        answer[positions[neighbour]] = neighbour

                    indegree[neighbour] -= 1
                    if indegree[neighbour] == 1:
                        queue.append(neighbour)
                        visited.add(neighbour)




        return answer