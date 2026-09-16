class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for c1 in text1:
            prev = 0

            for j, c2 in enumerate(text2, 1):
                temp = dp[j]

                if c1 == c2:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])

                prev = temp

        return dp[-1]