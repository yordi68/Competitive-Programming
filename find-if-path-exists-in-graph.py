class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        #Basic Implementation of Quick Union and Quick Find....
        #Both are fast

        parent = {i : i for i in range(n)} 
        size = [1] * n


        def find(node):
            if parent[node] == node:
                return node
            grandParent = find(parent[node])
            parent[node] = grandParent
            return grandParent

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


        for From, To in edges:
            union(From, To)

        # print(parent)

        return find(source) == find(destination)