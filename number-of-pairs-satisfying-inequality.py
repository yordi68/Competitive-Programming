class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.count = 0
        self.diff = diff
        dif = []
        for i in range(len(nums1)):
            dif.append(nums1[i] - nums2[i])
        self.mergeSort(dif, 0, len(dif) - 1)
        return self.count
        

    def mergeSort(self, arr, left, right):
        if left == right:
            return [arr[left]]
        mid = left + (right - left) // 2
        left = self.mergeSort(arr, left, mid)
        right = self.mergeSort(arr, mid + 1, right)
        return self.merge(left, right)

    def merge(self, left, right):
        i = 0
        j = 0
        while i < len(left):
            while j < len(right) and left[i] - self.diff > right[j] :
                j += 1
            self.count += len(right) - j             
            i += 1

        i = 0
        j = 0
        ans = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1

        while i < len(left):
            ans.append(left[i])
            i += 1
        while j < len(right):
            ans.append(right[j])
            j += 1

        return ans