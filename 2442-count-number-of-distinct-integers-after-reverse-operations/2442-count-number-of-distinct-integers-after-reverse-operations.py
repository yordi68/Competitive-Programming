class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        temp = nums.copy()
        
        for number in nums:
            reverse = 0
            while number > 0:
                lastdigit = number % 10
                reverse = (reverse * 10) + lastdigit
                number = number // 10
            temp.append(reverse)
            
        return len(set(temp))
            