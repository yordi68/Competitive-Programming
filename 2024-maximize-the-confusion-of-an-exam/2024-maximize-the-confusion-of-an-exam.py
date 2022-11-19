class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxf = i = 0
        count = collections.Counter()
        for j in range(len(answerKey)):
            count[answerKey[j]] += 1
            maxf = max(maxf, count[answerKey[j]])
            if j - i + 1 > maxf + k:
                count[answerKey[i]] -= 1
                i += 1
        return len(answerKey) - i