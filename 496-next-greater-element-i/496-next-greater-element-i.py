class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, map = [], {}
        for i in range(len(nums2))[::-1]:
            num = nums2[i]
            while stack and num > stack[-1]:
                stack.pop()
            map[num] = stack[-1] if stack else -1
            stack.append(num)
        return ([map[num] for num in nums1])