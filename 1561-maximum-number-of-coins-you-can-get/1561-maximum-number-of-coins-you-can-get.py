class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sor_pile = sorted(piles,reverse = True)
        total = 0
        n = len(piles) // 3
        i = 1
        
        for _ in range(n):
            total += sor_pile[i]
            i += 2
            
        return total

        