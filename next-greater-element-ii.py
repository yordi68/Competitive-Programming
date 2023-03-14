class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        n = len(nums)
        stack = []
        for i in range(2 * n - 1)[::-1]:
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            if i < n:
                if stack:
                    res[i] = stack[-1]
            stack.append(nums[i % n])

        return(res)