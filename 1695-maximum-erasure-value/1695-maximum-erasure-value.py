class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        cur_sum = 0
        seen = set()
        l = 0
        for r in range(len(nums)):
            while nums[r] in seen:
                seen.remove(nums[l])
                cur_sum -= nums[l]
                l += 1
            seen.add(nums[r])
            cur_sum += nums[r]
            res = max(res,cur_sum)
            
        return res
            