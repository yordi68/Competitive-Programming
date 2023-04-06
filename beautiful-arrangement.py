class Solution:
    def countArrangement(self, n: int) -> int:
        ans = 0
        curr = []
        used = 0
        nums = [i for i in range(1 , n + 1)]

        def build(i):
            nonlocal used , ans
            if curr and ( curr[-1] % len(curr) != 0) and (len(curr) % curr[-1] != 0):
                return

            if i == len(nums):
                ans += 1
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