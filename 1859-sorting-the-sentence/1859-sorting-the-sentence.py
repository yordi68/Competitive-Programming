class Solution:
    def sortSentence(self, s: str) -> str:
         a = list(s.split())
         n = len(a)
         b = []
         for i in range(1, n+1):
            for x in range(n):
                 if i == int(a[x][-1]):
                     b.append(a[x])
                     break
         print(b)
         for j in b:
             index = int(j[-1]) - 1
             b[index] = j[:-1]
         return " ".join(b)
        