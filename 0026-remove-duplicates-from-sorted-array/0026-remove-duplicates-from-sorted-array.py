class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        
        while right < n:
            if nums[left] == nums[right]:
                right += 1
            elif nums[left] != nums[right]:
                nums[left + 1] = nums[right]
                left += 1
                
        return left + 1