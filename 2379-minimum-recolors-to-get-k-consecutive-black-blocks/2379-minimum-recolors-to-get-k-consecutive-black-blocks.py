class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        res = float("inf")
        l = r = 0

        while r < len(blocks):
            if blocks[r] == 'W':
                count += 1

            while (r - l + 1) == k:
                res = min(res, count)
                if blocks[l] == 'W':
                    count -= 1
                l += 1

            r += 1

        return(res)