class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for key , value in edges:
            adjList[key].append(value)

        check = set()
        for value in adjList.values():
            for number in value:
                check.add(number)

        ans = []
        for i in range(n):
            if i not in check:
                ans.append(i)
        
        return ans