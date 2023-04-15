class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.ans = []
        self.backtrack([0],0)
        return self.ans

    def backtrack(self,curr,i):
        if i == len(self.graph) - 1:
            self.ans.append(curr[:])
            return

        for idx in self.graph[i]:
            curr.append(idx)
            self.backtrack(curr,idx)
            curr.pop()