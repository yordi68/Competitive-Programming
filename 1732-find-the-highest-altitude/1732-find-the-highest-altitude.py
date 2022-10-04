class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0] + list(accumulate(gain))
        return(max(alt))