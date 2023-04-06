class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        used = 0
        def build(i):
            nonlocal used
            if i == len(nums):
                ans.append(curr[:])
                return

            for idx , num in enumerate(nums):
                if (used & (1 << idx)) == 0:
                    used |= (1 << idx)
                    curr.append(num)
                    build(i + 1)
                    curr.pop()
                    used ^= (1 << idx)

        build(0)
        return ans