class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        minLength = float("inf")

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                minLength = min(minLength, right - left+ 1)
                total -= nums[left]
                left += 1

        return minLength if minLength != float("inf") else 0
            