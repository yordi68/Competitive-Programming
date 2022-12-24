class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        
        left = 0
        right = n - 1
        count = 0

        while left <= right:
            if nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                count += 1
                left += 1
                right -= 1
            elif nums[right] == val and nums[left] != val:
                count += 1
                right -= 1
            elif nums[right] != val and nums[left] != val:
                left += 1
            elif nums[right] == val and nums[left] == val:
                count += 1
                right -= 1
        
        
        return n - count