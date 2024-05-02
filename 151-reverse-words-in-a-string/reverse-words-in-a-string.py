class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        Array = []

        for i in range(len(s)):
            if not s[i].isalnum():
                if stack:
                    Array.append(''.join(stack))
                    stack.clear()
            else: 
                stack.append(s[i])

        if stack:
            Array.append(''.join(stack))

        Array.reverse() 

        ans = ""
        for string in Array:
            ans += string
            ans += " "

        return ans.strip()
        

            
                