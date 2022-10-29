class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        set_nums = set(nums)
        if len(set_nums) == 1 and 1 in set_nums:
            return len(nums) - 1
        elif len(set_nums) == 1 and 0 in set_nums:
            return 0
        for i in range(1,len(nums)):
            if nums[i] == 0:
                l = r = i
                while l > 0 and nums[l - 1] == 1:
                    l -= 1
                while r < (len(nums) - 1) and nums[r + 1] == 1:
                    r += 1
                res = max(res, r - l)
        return res