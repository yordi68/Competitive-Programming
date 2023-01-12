class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows_num = len(strs)
        col_num = len(strs[0])
        column_del = 0
        for i in range(col_num):
            for j in range(rows_num - 1):
                if ord(strs[j][i]) > ord(strs[j + 1][i]):
                    column_del += 1
                    break
                    
        return column_del