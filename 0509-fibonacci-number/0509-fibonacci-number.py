class Solution:
    def fib(self, n: int) -> int:
        answer = [0] * (n + 1)
        
        if n == 0:
            return 0
        
        answer[0] = 0
        answer[1] = 1
        
        for state in range(2, n + 1):
            answer[state] = answer[state - 1] + answer[state - 2]
            
        return answer[n]
        
        
        
        