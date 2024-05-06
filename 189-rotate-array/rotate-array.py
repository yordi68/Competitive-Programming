class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverseArray(0, len(nums) - 1, nums)
        self.reverseArray(0, k - 1,nums)
        self.reverseArray(k, len(nums) - 1, nums)
        return nums

    def reverseArray(self, left: int, right: int, array: List[int]):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        