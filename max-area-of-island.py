class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0 , 1) , (0, -1), (1, 0) , (-1 ,0)]
        visited = set()
        area = 0
        def inBound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row, col):
            nonlocal area
            visited.add((row, col))
            area += 1

            for r,c in directions:
                newRow = row + r
                newCol = col + c
                
                if inBound(newRow, newCol) and (newRow, newCol) not in visited and grid[newRow][newCol] == 1:
                    dfs(newRow, newCol )
            return area
        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea, dfs(r, c))
                    area = 0

        return maxArea