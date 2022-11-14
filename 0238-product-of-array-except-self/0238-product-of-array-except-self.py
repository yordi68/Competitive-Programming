class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        
        
        
        result = [1] * len(nums)
        running_product = 1
        
        for i in range(len(nums)):
            result[i] = running_product
            running_product *= nums[i]
            
        running_product = 1
        
        for i in range(len(nums))[::-1]:
            result[i] = result[i] * running_product
            running_product *= nums[i]
            
        return(result)
