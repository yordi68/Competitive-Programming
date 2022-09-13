class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        i = 1
        while i < n:
            temp = nums[i]
            j = i-1
            while j >= 0 and nums[j] > temp:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = temp
            i += 1
        