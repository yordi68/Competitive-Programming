class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'}':'{',')':'(',']':'['}
        for p in s:
            if p in dict.values():
                stack.append(p)
            elif stack and stack[-1] == dict[p]:
                stack.pop()
            else:
                return (False)
        return len(stack) == 0
        
