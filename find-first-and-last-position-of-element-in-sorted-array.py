class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.start(nums,target),self.end(nums,target)]


    def start(self,nums,target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target and mid - 1 >= 0:
                    return mid
                else:
                    right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def end(self,nums,target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] != target and mid + 1 < len(nums):
                    return mid
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1