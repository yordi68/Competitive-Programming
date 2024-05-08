class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr = len(nums1) - 1
        for i in range(len(nums2)):
                nums1[ptr] = nums2[i]
                ptr -= 1
        nums1.sort()
