class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        
        while left <= right:
            if  (left * left) + (right * right) < c:
                left += 1
            elif  (left * left) + (right * right) > c:
                right -= 1
            elif (left * left) + (right * right) == c:
                return True
                

        
        return False