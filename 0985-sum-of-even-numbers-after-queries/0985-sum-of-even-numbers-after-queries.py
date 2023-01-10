class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        total = []
        Sum = 0
        for i in range(n):
            if nums[i] % 2 == 0:
                Sum += nums[i]

        for x,y in queries:
            if nums[y] % 2 != 0 and (nums[y] + x) % 2 == 0:
                Sum += nums[y] + x
            elif nums[y] % 2 == 0 and (nums[y] + x) % 2 == 0:
                Sum += x
            elif nums[y] % 2 == 0 and (nums[y] + x) % 2 != 0:
                Sum -= nums[y]
            nums[y] += x
            total.append(Sum)

        return(total)