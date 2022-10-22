class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        size = float("inf")
        total = 0
        while r < len(nums) and l < len(nums):
            total += nums[r]
            while total >= target and l <= r:
                size = min(size,r - l + 1)
                total -= nums[l]
                l += 1
            r += 1
        return size if size != float("inf") else 0