class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        prev = []
        res = False
        if len(num) <= 2:
            return False
        def backtrack(idx):
            nonlocal res
            if idx >= len(num) and len(prev) >= 3:
                res = True
                return

            for i in range(idx , len(num)):
                number = num[idx : i + 1]
                if len(number) > 1 and number[0] == "0":
                     return 

                if len(prev) < 2 or int(prev[-1]) + int(prev[-2]) == int(number):
                    prev.append(number)
                    backtrack(i + 1)
                    prev.pop()  
                
        backtrack(0)
        return res