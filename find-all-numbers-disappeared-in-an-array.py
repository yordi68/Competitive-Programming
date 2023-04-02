class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        countArr = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            countArr[nums[i]] += 1
        for i in range(len(countArr)):
            if countArr[i] == 0:
                ans.append(i)

        return ans[1:]