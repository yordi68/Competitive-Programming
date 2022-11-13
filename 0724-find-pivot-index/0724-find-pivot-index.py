class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = rightSum = 0
        total = sum(nums)
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if rightSum == leftSum:
                return(i)
            leftSum += nums[i]
        return -1
        