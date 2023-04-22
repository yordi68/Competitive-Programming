class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(left, right, k):
            if left == right:
                return nums[left]

            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]

            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            i = left - 1
            for j in range(left, right):
                if nums[j] >= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]

            nums[i+1], nums[right] = nums[right], nums[i+1]

            if i+1 == k-1:
                return nums[i+1]
            elif i+1 < k-1:
                return quickSelect(i+2, right, k)
            else:
                return quickSelect(left, i, k)
        
        return quickSelect(0, len(nums)-1, k)