    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = defaultdict(int)
        for i in range(V):
            if not visited[i]:
                if self.detect_cycle(i, adj, visited):
                    return True
        return False