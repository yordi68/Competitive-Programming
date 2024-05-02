class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        setOfNums = set(nums)
        largest = 0
        for number in nums:
            invert = -1 * number
            if number > 0 and (invert in setOfNums):
                largest = max(largest, number)
        
        return -1 if largest == 0 else largest