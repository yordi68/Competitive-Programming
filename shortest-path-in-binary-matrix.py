class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        queue = deque([(0, 0)])
        visited = set((0,0))
        
        n = len(grid)
        
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        def inBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        level = 1
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                if row == col == n - 1:
                    return level

                for r, c in directions:
                    nr = r + row
                    nc = c + col
                    if inBound(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == 0:
                        queue.append((nr, nc))
                        visited.add((nr, nc))

            level += 1

        return -1