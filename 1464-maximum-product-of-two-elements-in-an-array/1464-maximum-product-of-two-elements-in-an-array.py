class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        max_product = (nums[len(nums) - 1] - 1) * (nums[len(nums) - 2] - 1)
        return(max_product)