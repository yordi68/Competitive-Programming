class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = -1
        nums.sort()
        for i in range(len(nums)):
            xor = nums[i] ^ i
            if xor != 0:
                ans = i
                break

        return ans if ans != -1 else len(nums)