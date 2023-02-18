class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        idx_a = -1
        idx_b = -1
        idx_c = -1
        
        for i,x in enumerate(s):
            if x == 'a':
                idx_a = i
            elif x == 'b':
                idx_b = i
            else:
                idx_c = i
                
                
            if i > 1:
                count += min(idx_a,idx_b,idx_c) + 1
                
        return count