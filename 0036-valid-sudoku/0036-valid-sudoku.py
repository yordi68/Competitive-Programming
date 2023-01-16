class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    row = str(num) + "at row"+ str(i)
                    col = str(num) + "at col" +  str(j)
                    box = str(num) + "at box" + str(i // 3) + "," +  str(j // 3)
                    if row in seen or col in seen or box in seen :
                         return False
                    else:
                        seen.add(row)  
                        seen.add(col)  
                        seen.add(box)
        return True
                    
        