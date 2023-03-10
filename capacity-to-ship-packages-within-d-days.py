class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        capacity = right
        while left <= right:
            mid = left + (right - left) // 2
            if self.ship(mid,weights,days):
                capacity = min(mid,capacity)
                right = mid - 1
            else:
                left = mid + 1
        return capacity

    def ship(self,cap,weights,days):
        ships = 1
        currCap = cap
        for weight in weights:
            if currCap - weight < 0:
                ships += 1
                currCap = cap
            currCap -= weight
        return ships <= days