class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(1,n - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = right = i
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                    
                if left == 0 and right == n - 1:
                    return True
            
            
        return False