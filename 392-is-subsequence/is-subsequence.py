class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: 
            return True

        left = 0

        for character in t:
            if character == s[left]:
                left += 1
            
            if left == len(s):
                return True

        return False