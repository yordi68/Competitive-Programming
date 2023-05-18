class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        parent = {i : i for i in range(1, n + 1 )}
        size = [1] * (n + 1)


        def find(node):
            if parent[node] == node:
                return parent[node]

            allParent = find(parent[node])
            parent[node] = allParent

            return allParent

        def union(From, To):
            parentFrom = find(From)
            parentTo = find(To)

            if parentFrom == parentTo:
                return

            if size[parentFrom] > size[parentTo]:
                parent[parentTo] = parentFrom
                size[parentFrom] += size[parentTo]
            else:
                parent[parentFrom] = parentTo
                size[parentTo] += size[parentFrom]

        for node1, node2, distance in roads:
            union(node1, node2)

        minimumPath = float('inf')
        for node1, node2, distance in roads:
            if (find(node1) == find(1) or find(node2) == find(1))and distance < minimumPath:
                minimumPath = distance
            
        return minimumPath