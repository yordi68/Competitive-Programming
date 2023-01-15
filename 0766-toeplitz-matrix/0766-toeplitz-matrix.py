class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        from collections import defaultdict
        _diagonal = defaultdict(set)
        
        row = len(matrix)
        col = len(matrix[0])
        
        
        for i in range(row):
            for j in range(col):
                _diagonal[j - i].add(matrix[i][j])
        n = len(_diagonal)      
        for x in _diagonal.values():
            if len(x) > 1:
                return False
            
        return True
        