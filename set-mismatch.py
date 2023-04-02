class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = dict(Counter(nums))
        ans = []
        n = len(nums)
        for x , y in c.items():
            if y == 2:
                nums.remove(x)
                ans.append(x)
        
        nums = set(nums)
        for i in range(1 , n + 1):
            if i not in nums:
                ans.append(i)
        return ans