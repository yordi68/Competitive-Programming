class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum = count = 0
        for i in range(0,k-1):
            sum += arr[i]
        
        for i in range(k-1,len(arr)):
            sum += arr[i]
            if sum / k >= threshold:
                count += 1
            sum -= arr[i - k + 1]
        
        return count
                