class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res, l = 0, 0
        for r in range(len(nums)):
            if nums[r] == 0:                       
                if k == 0:                         
                    while nums[l] != 0 :
                        l += 1
                    l += 1
                else : 
                    k-= 1                      
            res = max(res, r - l + 1)              
        return res