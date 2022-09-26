class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            elif stack[-1].isupper() is True and s[i].isupper() is True:
                stack.append(s[i])
            elif stack[-1] == (s[i]).upper() or (stack[-1]).upper() == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return("".join(stack))