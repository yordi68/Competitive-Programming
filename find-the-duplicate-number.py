class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        countArr = [0] * len(nums)

        for i in range(len(nums)):
            if countArr[nums[i]] < 1:
                countArr[nums[i]] += 1
            else:
                return nums[i]