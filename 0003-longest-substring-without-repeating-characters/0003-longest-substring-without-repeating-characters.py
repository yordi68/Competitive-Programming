class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = longest = 0
        map = {}
        if len(s) < 2:
            return len(s)
        
        while r < len(s):
            if s[r] in map:
                longest = max(longest,r - l)
                l = max(l,map[s[r]] + 1)
            map[s[r]] = r
            r += 1
        return max(longest,r - l )