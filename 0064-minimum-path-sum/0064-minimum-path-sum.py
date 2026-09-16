class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dp = [float('inf')] * (cols + 1)
        dp[1] = 0

        for row in grid:
            for j in range(1, cols + 1):
                dp[j] = min(dp[j], dp[j - 1]) + row[j - 1]

        return dp[cols]
