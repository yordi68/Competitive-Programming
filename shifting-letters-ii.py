class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        prefixSum = [0 for _ in range(len(s) + 1)]

        for left , right , dxn in shifts:
            if dxn == 0:
                prefixSum[left] -= 1
                prefixSum[right + 1] += 1
            else:
                prefixSum[left] += 1
                prefixSum[right + 1] -= 1

        runningSum = 0
        for i in range(len(s)):
            runningSum += prefixSum[i]
            asci = (((ord(s[i]) + runningSum) - 97) % 26) + 97
            s = s[:i] + chr(asci) + s[i + 1:]

        return s