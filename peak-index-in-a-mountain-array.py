class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = l + (r - l) // 2

            if m == 0:
                if arr[m] > arr[m+1]:
                    return m
                else:
                    l = m+1

            elif arr[m-1] < arr[m] and arr[m] > arr[m+1]:
                return m

            elif arr[m-1] < arr[m]:
                l = m + 1
            else:
                r = m - 1