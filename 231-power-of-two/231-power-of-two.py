class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        elif n % 2 != 0:
            if n == 1:
                return True
            else:
                return False
        
        return self.isPowerOfTwo(n/2)

            