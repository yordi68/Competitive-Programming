class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefixSum = [0] * len(nums)

        for req in requests:
            prefixSum[req[0]] += 1
            if (req[1] + 1) < len(nums):
                prefixSum[req[1] + 1] -= 1

        prefixSum = list(accumulate(prefixSum))
        prefixSum.sort(reverse=True)
        nums.sort(reverse=True)

        total = 0
        for i in range(len(nums)):
            total += (nums[i] * prefixSum[i])

        return total % (10 ** 9 + 7)