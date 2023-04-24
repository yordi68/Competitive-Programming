class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        import math
        li = Counter(deck)
        val = li.values()
        m = math.gcd(*val) 
        if m >= 2:
            return True 
        else:
            return False