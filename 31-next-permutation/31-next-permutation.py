class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) <= 2:
             return nums.reverse()
        r = len(nums) - 2
        while r >= 0 and nums[r] >= nums[r + 1]:
              r -= 1
        if r == -1:
            return nums.reverse()
        for i in range(len(nums) - 1,r,-1):
              if nums[r] < nums[i]:
                    nums[i],nums[r]=nums[r],nums[i]
                    break
        nums[r + 1:] = reversed(nums[r + 1:])
        