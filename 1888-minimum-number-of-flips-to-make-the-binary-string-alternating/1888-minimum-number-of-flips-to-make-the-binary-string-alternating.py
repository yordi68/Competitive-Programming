class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        string1 = ""
        string2 = ""
        for i in range(len(s)):
            string1 += "0" if  i % 2 else "1"
            string2 += "1" if  i % 2 else "0"
            
        res = len(s)
        dif1 = 0
        dif2 = 0
        l = 0
        for r in range(len(s)):
            if s[r] != string1[r]:
                dif1 += 1
            if s[r] != string2[r]:
                dif2 += 1
                
            if (r - l + 1) > n:
                if s[l] != string1[l]:
                    dif1 -= 1
                if s[l] != string2[l]:
                    dif2 -= 1
                l += 1
                
            if (r - l + 1) == n:
                res = min(res,dif1,dif2)
                
        return res