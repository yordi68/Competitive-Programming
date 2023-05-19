class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {chr(i + 97) : chr(i + 97) for i in range(26)}

        size = {chr(i + 97) : 1 for i in range(26)}
      
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

        for i in range(len(equations)):
            if equations[i][1] == '=':
                union(equations[i][0], equations[i][3])


        for i in range(len(equations)):
            if equations[i][1] == '!':
                if find(equations[i][0]) == find(equations[i][3]):
                        return False

        return True