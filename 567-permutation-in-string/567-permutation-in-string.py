class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return []
        s1count,s2count = {},{}
        for i in range(len(s1)):
            s1count[s1[i]] = 1 + s1count.get(s1[i],0)
            s2count[s2[i]] = 1 + s2count.get(s2[i],0)
        res = True if s1count ==s2count else False
        l = 0
        for r in range(len(s1),len(s2)):
            s2count[s2[r]] = 1 + s2count.get(s2[r],0)
            s2count[s2[l]] -= 1
            if s2count[s2[l]] == 0:
                s2count.pop(s2[l])
            l += 1
            if s2count == s1count:
                res = True
        return res