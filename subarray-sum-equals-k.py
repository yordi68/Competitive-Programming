class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        runningSum = 0
        map = defaultdict(int)
        count = 0

        for i in range(len(nums)):
            runningSum += nums[i]
            if runningSum == k:
                count += 1
            if (runningSum - k) in map:
                count += map[runningSum - k]
            map[runningSum] += 1

        return count