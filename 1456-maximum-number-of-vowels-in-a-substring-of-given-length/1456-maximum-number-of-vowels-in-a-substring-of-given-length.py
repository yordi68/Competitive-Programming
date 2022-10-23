class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ['a','e','i','o','u']
        res,count = 0,0
        for idx,char in enumerate(s):
            if char in vowel:
                count += 1
            if idx >= k and s[idx - k] in vowel:
                count -= 1
            res = max(res,count)
        return res