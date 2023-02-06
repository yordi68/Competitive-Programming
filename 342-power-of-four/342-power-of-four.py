class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        elif n % 4 != 0:
            if n == 1:
                return True
            else:
                return False
            
        return self.isPowerOfFour(n/4)
            
        