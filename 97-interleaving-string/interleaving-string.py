class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # Length check
        if len(s1) + len(s2) != len(s3):
            return False

        m = len(s1)
        n = len(s2)

        # dp[i][j] means:
        # Can s3[:i+j] be formed using s1[:i] and s2[:j]?
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty strings can form an empty string
        dp[0][0] = True

        # Use only s1
        for i in range(1, m + 1):
            dp[i][0] = (
                dp[i - 1][0]
                and s1[i - 1] == s3[i - 1]
            )

        # Use only s2
        for j in range(1, n + 1):
            dp[0][j] = (
                dp[0][j - 1]
                and s2[j - 1] == s3[j - 1]
            )

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # Current character in s3
                k = i + j - 1

                # Take character from s1
                from_s1 = (
                    dp[i - 1][j]
                    and s1[i - 1] == s3[k]
                )

                # Take character from s2
                from_s2 = (
                    dp[i][j - 1]
                    and s2[j - 1] == s3[k]
                )

                dp[i][j] = from_s1 or from_s2

        return dp[m][n]
