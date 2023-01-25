#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        right = 0
        while right < n - 1:
            if arr[right] > arr[right + 1]:
                return 0
            right += 1
                
        return 1
            
