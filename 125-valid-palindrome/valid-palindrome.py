class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = ""

        for i in range(len(s)):
            if s[i].isalnum():
                phrase += s[i].lower()
        
        return phrase == phrase[::-1]