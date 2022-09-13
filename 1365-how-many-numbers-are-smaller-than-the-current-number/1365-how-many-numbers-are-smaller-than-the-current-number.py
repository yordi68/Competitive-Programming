class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
         n = len(nums)
         b = []
         i = 0
         while i < n:
             max1 = i
             temp = nums[max1]
             count = 0
             j = 0
             while j < n:
                 if nums[max1] > nums[j]:
                     count += 1
                 j += 1
             b.append(count)
             i += 1
         return(b)
        