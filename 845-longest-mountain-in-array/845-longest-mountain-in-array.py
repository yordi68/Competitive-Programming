class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0
        for x in range(1,len(arr) - 1):
            if arr[x-1] < arr[x] > arr[x+1]:
                l=r=x
                while l>0 and arr[l]>arr[l-1]:
                    l-=1
                while r<len(arr) - 1 and arr[r] > arr[r+1]:
                    r+=1
                res = max(res,r-l+1)
        return res