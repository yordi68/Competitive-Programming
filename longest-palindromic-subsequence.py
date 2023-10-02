class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        m = len(s)

        strRev = s[::-1]
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

        for r in range(n + 1):
            dp[r][0] = 0
        for c in range(m + 1):
            dp[0][c] = 0

        for r in range(1, n + 1):
            for c in range(1, m + 1):
                if strRev[r - 1] == s[c - 1]:
                    dp[r][c] = 1 + dp[r - 1][c - 1]
                else:
                    dp[r][c] = 0 + max(dp[r - 1][c], dp[r][c - 1])

        return dp[n][m ]