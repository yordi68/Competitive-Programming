class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        z = "".join(ch for ch in s if ch.isalnum())
        s = "".join(ch for ch in s if ch.isalnum())
        a = list(s)
        l,r = 0,len(s) - 1
        while l < r:
            a[l],a[r] = a[r],a[l]
            l += 1
            r -= 1
        s = "".join(a)
        if z==s:
            return(True)
        else:
            return(False)