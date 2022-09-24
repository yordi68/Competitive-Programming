class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        count = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')' and stack[-1] == '(':
                count.append(len(stack))
                stack.pop()
        return(max(count,default=0))