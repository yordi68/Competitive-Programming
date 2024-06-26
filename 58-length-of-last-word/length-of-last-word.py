class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1
        
        lastChrIndex = i

        while i >= 0 and s[i] != ' ':
            i -= 1
        
        return lastChrIndex - i