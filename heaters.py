class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        max_ = 0
        for house in houses:
             max_ = max(max_, self.binarySearch(house, heaters))

        return max_

    def binarySearch(self, val, heaters):
        left = 0
        right = len(heaters) - 1
        dist = float("inf")

        while left <= right:
            mid = left + (right - left) // 2
            dist = min(dist, abs(heaters[mid] - val))
            if val < heaters[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return dist