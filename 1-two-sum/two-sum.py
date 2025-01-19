class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        nums_index = []

        for i, num in enumerate(nums):
            nums_index.append([num, i])

        nums_index = sorted(nums_index, key=lambda x: x[0])

        while left != right:
            print(nums_index[left][0])
            print(nums_index[right][0])  

            if nums_index[left][0] + nums_index[right][0] == target:
                return [nums_index[left][1], nums_index[right][1]]
            elif nums_index[left][0] + nums_index[right][0] > target:
                right -= 1
            else:
                left += 1

