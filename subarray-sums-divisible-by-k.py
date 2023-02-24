class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        runningSum = 0
        remainder_count = defaultdict(int)
        count = 0
        
        for i in range(n):
            runningSum += nums[i]
            remainder = runningSum % k
            if remainder in remainder_count:
                count += remainder_count[remainder]

            if remainder == 0:
                count += 1
            remainder_count[remainder] += 1

        return count