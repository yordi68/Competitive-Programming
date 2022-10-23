class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        size = 0
        set_nums = set(nums)
        if len(set_nums) == 1 and 0 in set_nums:
            return 0
        elif len(set_nums) == 1 and 1 in set_nums:
            return(len(nums) - 1)   
        for idx in range(len(nums)):
            if nums[idx] == 0:
                l=r=idx
                while l > 0 and nums[l - 1] == 1:
                    l -= 1
                while r < (len(nums) - 1) and nums[r + 1] == 1:
                    r += 1
                size = max(size,r - l)
        return size