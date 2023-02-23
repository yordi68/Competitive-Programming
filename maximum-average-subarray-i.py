class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_average = float("-inf")
        left = 0
        total = 0
        
        for right in range(n):
            total += nums[right]
            if (right - left + 1 == k):
                max_average = max(total / k,max_average)
                total -= nums[left]
                left += 1
                
        return max_average