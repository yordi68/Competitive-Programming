class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        countArr = [0] * (len(nums) + 1)
        ans = []
        for i in range(len(nums)):
            if countArr[nums[i]] < 1:
                countArr[nums[i]] += 1
            else:
                ans.append(nums[i])
        
        return ans