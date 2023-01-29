#User function Template for python3

class Solution: 
    def select(self, l, i):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                i = j
        return i
    
    def selectionSort(self, l,n):
        for i in range(len(l)):
            j = self.select(l, i)
            l[i], l[j] = l[j], l[i]
                
        return l
      
