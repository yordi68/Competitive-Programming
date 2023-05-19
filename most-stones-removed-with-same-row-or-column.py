class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {i : i for i in range(len(stones))}

        size = [1] * len(stones)


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
                return
            if size[parentFrom] > size[parentTo]:
                parent[parentTo] = parentFrom
                size[parentFrom] += size[parentTo]
            else:
                parent[parentFrom] = parentTo
                size[parentTo] += size[parentFrom]

        for i in range(len(stones)):
            for j in range(len(stones)):
                if stones[j][0] == stones[i][0] or stones[i][1] == stones[j][1]:
                    union(i, j)

        
        visited = set()
        for stone in parent.keys():
            visited.add(find(stone))


        return len(stones) - len(visited)