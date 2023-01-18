class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        temp = nums.copy()
        temp_set = set()
        
        for number in nums:
            reverse = 0
            while number > 0:
                lastdigit = number % 10
                reverse = (reverse * 10) + lastdigit
                number = number // 10
            temp.append(reverse)
            
        temp_set = set(temp)
        return len(temp_set)
            