class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        transpose  = [[0 for _ in range(rows)] for _ in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                transpose[j][i] = grid[i][j]
                
        total = 0
        for i in range(rows):
            for j in range(rows):
                if grid[i] == transpose[j]:
                     total += 1
                
        return total
        
        