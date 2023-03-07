class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        stack = []

        for i in range(len(arr) + 1):

            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                deleted = stack.pop()
                left_distance = -1 if not stack else stack[-1]
                right_distance = i
                count = (deleted - left_distance) * (right_distance - deleted)
                res += (count * arr[deleted])

            stack.append(i)
        return res % (10 ** 9 + 7)