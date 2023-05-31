class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        memo[-2][-2] = 1
        
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1 and col == n - 1:
                    continue
                memo[row][col] = memo[row + 1][col] + memo[row][col + 1]
        
        return memo[0][0]
        
                
                
            
            
            
        