class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        l1 = l2 = 0
        while l1 < m and l2 < n:
            if nums1[l1] > nums2[l2]:
                temp.append(nums2[l2])
                l2 += 1
            else:
                temp.append((nums1[l1]))
                l1 += 1
        while l1 < m:
            temp.append((nums1[l1]))
            l1 += 1
        while l2 < n:
            temp.append(nums2[l2])
            l2 += 1
        nums1[:] = temp