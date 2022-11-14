class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = total = 0
        size = float("inf")
        
        while r < len(nums):
            total += nums[r]
            while total >= target:
                size = min(size,r - l + 1)
                total -= nums[l]
                l += 1
            r += 1
            
            
        return size if size != float("inf") else 0