class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        dicts1 = Counter(s1)
        windowdict = defaultdict(int)
        left = 0
        
        if len(s1) > len(s2):
            return False
            
        for right in range(n):
            windowdict[s2[right]] += 1
            
            if (right - left + 1) == len(s1):
                if dicts1 == windowdict:
                    return True
                windowdict[s2[left]] -= 1
                if windowdict[s2[left]] == 0:
                    del windowdict[s2[left]]
                left += 1
                
        return False