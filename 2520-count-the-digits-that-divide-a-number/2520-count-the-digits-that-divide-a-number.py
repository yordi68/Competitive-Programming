class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        temp = num
        while temp > 0:
            rem = temp % 10
            if num % rem == 0:
                count += 1
            
            temp = temp // 10
            
                
        return count