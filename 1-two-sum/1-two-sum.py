class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {val: idx for idx, val in enumerate(nums)}
        for idx, num in enumerate(nums):
            if target - num in my_dict and my_dict[target - num] != idx:
                return([idx, my_dict[target - num]])