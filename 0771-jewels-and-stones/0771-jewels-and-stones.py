class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        lookup = set()
        # copying the elements in jewels into the set
        for jewel in jewels:
            lookup.add(jewel)
        #iterating through the stones array and incrementing the total if the stone exists in the jewels set
        for stone in stones:
            if stone in lookup:
                total += 1
        return(total)