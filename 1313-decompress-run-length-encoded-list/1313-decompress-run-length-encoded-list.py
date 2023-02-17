class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        freq = nums[0]
        res = []
        for num in nums[1:]:
            if freq is not None:
                for i in range(freq):
                    res.append(num)
                freq = None
            else:
                freq = num
        return res
            
            