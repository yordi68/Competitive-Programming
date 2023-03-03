class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:

        runningSum = 0
        remainder = defaultdict(int)
        remainder[0] = 1
        total = 0

        for i in range(len(nums)):
            runningSum += nums[i]
            if runningSum - k in remainder:
                total += remainder[runningSum - k]
                
            remainder[runningSum] += 1
        return total