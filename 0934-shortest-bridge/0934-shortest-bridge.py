class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        visited = set()

        def inBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid)
                         
        def dfs(row, col):
            visited.add((row, col))
            for r, c in directions:
                newRow = r + row
                newCol = c + col
                if inBound(newRow, newCol) and grid[newRow][newCol] and (newRow, newCol) not in visited:
                    dfs(newRow, newCol)

        def bfs():
            level = 0
            queue = deque(visited)
            while queue:
                for i in range(len(queue)):
                    row, col = queue.popleft()
                    for r, c in directions:
                        newRow = row + r
                        newCol = col + c
                        if not inBound(newRow, newCol) or (newRow, newCol) in visited:
                            continue
                        if grid[newRow][newCol]:
                            return level
                        queue.append((newRow, newCol))
                        visited.add((newRow, newCol))
                level += 1

        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs() 


