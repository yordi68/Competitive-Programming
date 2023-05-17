class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i : i for i in range(1, len(edges) + 1)}
        size = [1] *  (len(edges) + 1)
        self.toBeDeleted = []


        def find(node):
            if parent[node] == node:
                return node

            allParent = find(parent[node])
            parent[node] = allParent

            return allParent

        def union(From, To):
            parentFrom = find(From)
            parentTo = find(To)

            if parentFrom == parentTo:
                self.toBeDeleted = [From, To]
                return

            if size[parentFrom] > size[parentTo]:
                parent[parentTo] = parentFrom
                size[parentFrom] += size[parentTo]
            else:
                parent[parentFrom] = parentTo
                size[parentTo] += size[parentFrom]

        for From, To in edges:
            union(From, To)

        return self.toBeDeleted