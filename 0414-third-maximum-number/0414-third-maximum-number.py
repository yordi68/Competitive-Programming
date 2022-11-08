class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums1 = list(set(nums))
        nums2 = list(sorted(nums1,key=None,reverse=True))
        if len(nums2) > 2:
            return nums2[2]
        else:
            return max(nums2)