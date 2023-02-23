class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        window_sum = 0
        left = 0
        windowlen = float("inf")
        
        for right in range(n):
            window_sum += nums[right]
            
            while window_sum >= target:
                windowlen = min(windowlen , right - left + 1)
                window_sum -= nums[left]
                left += 1
                
        return windowlen if windowlen != float("inf") else 0