class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
    
        parent = { chr(i + 97) : chr(i + 97) for i in range(26)}

        def find(char):
            if parent[char] == char:
                return char

            allParent = find(parent[char])
            parent[char] = allParent

            return allParent


        def union(From, To):
            parentFrom = find(From)
            parentTo = find(To)

            if parentFrom == parentTo:
                return

            if ord(parentFrom) > ord(parentTo):
                parent[parentFrom] = parentTo
            else:
                parent[parentTo] = parentFrom

        for i in range(len(s1)):
            union(s1[i], s2[i])

        ans = []
        for i in range(len(baseStr)):
            ans.append(find(baseStr[i]))

        return "".join(ans)