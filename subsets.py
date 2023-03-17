class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(cur , path):
            if cur >= len(nums):
                ans.append(path[:])
                return
            ans.append(path[:])
            for i in range(cur , len(nums)):
                path.append(nums[i])
                backtrack(i + 1 , path)
                path.pop()
            

        backtrack(0 , [])
        return ans