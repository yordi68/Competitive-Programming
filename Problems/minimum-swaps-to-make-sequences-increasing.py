class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        if n <= 1:
            return 0
        
        swap = [float("inf")] * n
        keep = [float("inf")] * n
        
        swap[0] = 1
        keep[0] = 0

        
        for i in range(1, n):
            if nums1[i - 1] < nums1[i] and nums2[i - 1] < nums2[i]:
                keep[i] = keep[i - 1]
                swap[i] = swap[i - 1] + 1
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                keep[i] = min(keep[i], swap[i - 1])
                swap[i] = min(swap[i], keep[i - 1] + 1)
                
        print(swap)
        print(keep)
        
        return min(swap[n - 1], keep[n - 1])
    
