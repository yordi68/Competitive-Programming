class Solution:
    def countDigits(self, num: int) -> int:
        num_list = []
        count = 0
        temp = num
        while temp > 0:
            num_list.append(temp % 10)
            temp = temp // 10
            
        n = len(num_list)
        for i in range(n):
            if num % num_list[i] == 0:
                count += 1
                
        return count