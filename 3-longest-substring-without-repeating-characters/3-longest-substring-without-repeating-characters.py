class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:      
        s = list(s)
        l,r,size = 0,0,0
        x = []
        while r < len(s):
            x.append(s[r])
            while len(x) != len(set(x)):
                x.pop(0)
                l += 1
            size = max(size,r - l + 1)
            r += 1
        return(size)