class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = r = sum = count = 0
        
        while r < len(arr):
            sum += arr[r]
            
            if r >= k - 1:
                if sum / k >= threshold:
                    count += 1
                sum -= arr[l]
                l += 1
            r += 1
        return count