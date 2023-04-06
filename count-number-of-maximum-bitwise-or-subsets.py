class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        length = 2 ** (len(nums))
        hash = defaultdict(int)
        for i in range(length):
            nor = 0
            n = i
            count = 0
            while n:
                if n & 1 != 0:
                    nor |= nums[count]
                n >>= 1
                count +=  1
            hash[nor] += 1
        return max(hash.values())