class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def inBound(row, col):
            return 0 <= row < len(grid2) and 0 <= col < len(grid2[0])

        def dfs(row, col):
            if (row, col) in visited:
                return True
            if grid2[row][col] == 0:
                return True
            visited.add((row, col))
            res = True
            if grid1[row][col] == 0:
                res = False

            for newRow, newCol in directions:
                newRow = row + newRow
                newCol = col + newCol
                if inBound(newRow, newCol) and grid2[newRow][newCol] and (newRow, newCol) not in visited:
                    res &= dfs(newRow, newCol)

            return res

        cnt = 0
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] == 1 and (row, col) not in visited and dfs(row, col):
                    cnt += 1

        return cnt