class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = []
        l,size= 0,0
        for r in range(len(s)):
            char_set.append(s[r])
            while len(char_set) != len(set(char_set)):
                char_set.pop(0)
                l += 1
            size = max(size, r - l + 1)
        return size
        

                