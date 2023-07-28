class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        visted = set()
        
        def inbound(row, col):
            return (0 <= row < len(board)) and (0 <= col < len(board[0]))


        def dfs(row, col, board):
            count = 0

            if board[row][col] == "M":
                board[row][col] = "X"
                return

            for r, c in directions:
                newRow = row + r
                newCol = col + c

                if inbound(newRow, newCol) and board[newRow][newCol] == "M":
                    count += 1
            if count > 0:
                board[row][col] = str(count)
                return

            board[row][col] = "B"
            
            for r, c in directions:
                newRow = row + r
                newCol = col + c
                if inbound(newRow, newCol)  and board[newRow][newCol] == "E":
                        dfs(newRow, newCol, board)
            
           
        dfs(click[0], click[1], board)
        return board