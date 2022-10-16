class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        """
        arr = [2,1,4,7,3,2,5]
                    l  r 
                 r - l + 1
        res = 0
        arr = [2,3,4,3,2,1,7,8,1]
                             lr
        arr = [1,2,3,4,5,4,3,2,1] #9
               0 1 2 3 4 5 6 7 8
        [48,62,39]#3 r < 2
         l      r
        """
        res = 0
        for i in range(1,len(arr) - 1):#8
            if arr[i - 1] < arr[i] > arr[i + 1]:
                l=r=i
                while l > 0 and arr[l - 1] < arr[l]:
                    l -= 1
                while r < (len(arr)  - 1)and arr[r + 1] < arr[r]:
                    r += 1
                res = max(res,r - l + 1)
        return res