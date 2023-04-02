class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]

            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)

            return merge(left_half, right_half)


        def merge(lh , rh):
            left = 0
            right = 0
            arr = []
            nonlocal ans
            i = 0
            j = 0
            while i < len(lh):
                while j < len(rh) and lh[i] > 2 * rh[j]:
                    j += 1
                ans += j
                
                i += 1

            while left < len(lh) and right < len(rh):
                if lh[left] <= rh[right]:
                    arr.append(lh[left])
                    left += 1
                else:
                    arr.append(rh[right])
                    right += 1
            
            while left < len(lh):
                arr.append(lh[left])
                left += 1
            while right < len(rh):
                arr.append(rh[right])
                right += 1

            return arr

        a = mergeSort(0, len(nums) - 1, nums)
        return ans