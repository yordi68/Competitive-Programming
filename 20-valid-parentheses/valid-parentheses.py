class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ")": "(",
            "]": "[",
            "}": "{",
        }


        for chr in s:
            if chr in pair:
                if stack and stack[-1] == pair[chr]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(chr)


        return True if len(stack) == 0 else False