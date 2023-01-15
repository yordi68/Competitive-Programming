class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        
        if row * col != r * c:
            return mat
        
        res = [[0] * c for _ in range(r)]
        m = r * c
        for i in range(m):
            res[i // c][i % c] = mat[i // col][i % col]
            
        return res
        

        