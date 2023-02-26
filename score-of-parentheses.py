class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        balanced = 0
        score = 0

        for i in range(len(s)):
            if s[i] == '(':
                balanced += 1
            else:
                balanced -= 1
                if s[i - 1] == '(':
                    score += pow(2,balanced)

        return score