class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i in range(1 , len(nums) + 2):
            if i not in count:
                return i