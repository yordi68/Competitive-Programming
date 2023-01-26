class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l <= r:
            area = min(height[l],height[r]) * (r - l)
            res = max(area,res)
            if height[l] < height[r]:
                l += 1
            elif height[r] == height[l]:
                l += 1
                r -= 1
            else:
                r -= 1
        return(res)