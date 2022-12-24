class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        
        left = 0
        right = n - 1
        count = 0

        while left <= right:
            # pass the number if it is not equal to value
            while left <= right and nums[left] != val:
                left += 1
            # pass the number if it is equal to the value   
            while left <= right and nums[right] == val:
                count += 1
                right -= 1
            # swap the value at the left and the right pointer
            if left <= right:
                nums[left], nums[right] = nums[right] , nums[left]
                count += 1
                left += 1
                right -= 1
                
        # return the lenght of the nums minus the value of the count
        return n - count