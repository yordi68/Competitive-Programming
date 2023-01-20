class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        if len(matrix) == 0:
            return res
        
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = -1
        
        while True:
            for i in range(n):
                col = col + 1
                res.append(matrix[row][col])
            m = m - 1
            if m == 0: break
            for i in range(m):
                row = row + 1
                res.append(matrix[row][col])
            n = n - 1
            if n == 0: break
            for i in range(n):
                col = col - 1
                res.append(matrix[row][col])
            m = m - 1
            if m == 0: break
            for i in range(m):
                row = row - 1
                res.append(matrix[row][col])
            n = n - 1
            if n == 0: break
                
        return res
                
                
                
                
        
