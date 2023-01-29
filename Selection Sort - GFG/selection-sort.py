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


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends