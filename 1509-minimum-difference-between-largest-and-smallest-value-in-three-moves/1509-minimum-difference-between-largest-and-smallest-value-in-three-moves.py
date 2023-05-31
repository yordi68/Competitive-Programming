class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums) <= 4:
            return 0

        left = nums[-1] - nums[3]
        right = nums[-4] - nums[0]
        x = nums[-3] - nums[1]
        y = nums[-2] - nums[2] 
        
        return min(left, right, x, y)