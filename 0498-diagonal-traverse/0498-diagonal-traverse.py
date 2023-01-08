class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat and not mat[0]:
            return []
        rows = len(mat)
        col = len(mat[0])
        diagonals = [[] for _ in range(rows + col - 1)] 
        
        for i in range(rows):
            for j in range(col):
                diagonals[i + j].append(mat[i][j])
        
        res = diagonals[0]
        for x in range(1,len(diagonals)):
            if x % 2 == 1:
                res.extend(diagonals[x])
            else:
                res.extend(diagonals[x][::-1])
                
        return res
            