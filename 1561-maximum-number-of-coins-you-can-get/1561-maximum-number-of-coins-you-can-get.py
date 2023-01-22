class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        total = 0
        n = len(piles) // 3
        
        i = 1
        for _ in range(n):
            total += piles[i]
            i += 2
            
        return total

        