class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        negCnt = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                negCnt += 1
            nums[i] = abs(nums[i])

        d = defaultdict(int)
        for i in range(len(nums)):
            idx = 0
            while nums[i]:
                if nums[i] & 1 == 1:
                    d[idx] += 1
                nums[i] >>= 1
                idx += 1

        ans = 0
        for key , value in d.items():
            if value % 3 != 0:
                ans += (1 << key)
        if negCnt % 3 == 0:
            return ans

        return -ans