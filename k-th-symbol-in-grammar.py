class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
          return 0
        length = 2 ** (n - 1)
        if length / 2 < k:  
            k = k - (length / 2)
            return self.invert(self.kthGrammar(n - 1 , k))
        return self.kthGrammar(n - 1 , k)


    def invert(self, s):
        if s == 0:
            return 1
        return 0