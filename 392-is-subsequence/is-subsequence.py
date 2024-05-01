class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        left = 0
        
        for right in range(len(t)):
            if left < len(s) and s[left] == t[right]:
                left += 1

        return True if left == len(s) else False

        