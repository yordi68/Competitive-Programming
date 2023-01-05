class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        # change the string jewels into a set
        jewels = set(jewels)
        n = len(stones) 
        #iterating through the stones array and incrementing the total if the character exists in the jewels set
        for i in range(n):
            if stones[i] in jewels:
                total += 1
        return(total)