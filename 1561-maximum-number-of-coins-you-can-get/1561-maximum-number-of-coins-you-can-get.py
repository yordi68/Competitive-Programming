class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        count = 0
        total = 0
        r = n
        c = 0
        itr = n // 3
        for i in range(n):
            count += 1
            r -= 1
            if count == 2 and itr != c:
                c += 1
                total += piles[r]
                count = 0
                
        return total
        