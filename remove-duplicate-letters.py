class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        check = set()

        for char in s:

            while stack and ord(stack[-1]) >= ord(char) and counter[stack[-1]] > 1:
                if char in check:
                    counter[char] -= 1
                    break
                deleted = stack.pop()
                counter[deleted] -= 1
                check.remove(deleted)

            if  not char in check:
                stack.append(char) 
                check.add(char)

        return ''.join(stack)