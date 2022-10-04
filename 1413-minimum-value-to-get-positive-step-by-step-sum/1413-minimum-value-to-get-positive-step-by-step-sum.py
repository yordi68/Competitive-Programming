class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        nums = list(itertools.accumulate(nums))
        print(nums)
        if min(nums) < 0:
            a = min(nums)
            a = (a * (-1)) + 1
            return(a)
        else:
            return(1)