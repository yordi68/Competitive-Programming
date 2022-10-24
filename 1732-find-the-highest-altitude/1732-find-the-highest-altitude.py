class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = [0]
        for idx in range(1,len(gain) + 1):
            prefix_sum.append(prefix_sum[idx - 1] + gain[idx - 1])
        return max(prefix_sum)