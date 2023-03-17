class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        nums = [i for i in range(1 , n + 1)]

        def backtrack(cur , k , path):

            if len(path) == k:
                ans.append(path[:])
                return 
            if cur >= len(nums):
                return


            for i in range(cur , len(nums)):
                path.append(nums[i])
                backtrack(i + 1 , k ,  path)
                path.pop()
            

        backtrack(0 , k , [])
        return ans