class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        i = 0
        while i < len(nums):
            if original == nums[i]:
                original = original * 2
                i = 0
                continue
            i += 1
        return(original)