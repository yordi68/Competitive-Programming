class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = list(accumulate(nums))
        return ans