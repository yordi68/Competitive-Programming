class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxSum = sum(cardPoints[:k])
        Sum = sum(cardPoints[:k])
        left = k - 1
        right = len(cardPoints) - 1

        while left != -1:
            Sum -= cardPoints[left]
            left -= 1
            Sum += cardPoints[right]
            right -= 1
            maxSum = max(maxSum, Sum)
        return maxSum