class Solution:
    def fib(self, n: int) -> int:
        
        
        if n == 0:
            return 0
        
        zero = 0
        one = 1
        
        
        
        for state in range(2, n + 1):
            temp = one
            one = zero + one
            zero = temp 
            
        return one
        
        
        
        