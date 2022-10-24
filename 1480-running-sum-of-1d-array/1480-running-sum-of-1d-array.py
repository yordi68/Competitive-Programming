class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = [0]
        for idx in range(1,len(nums) + 1):
            prefix_sum.append(prefix_sum[idx - 1] + nums[idx - 1])
        return prefix_sum[1:]