class Solution:
    def totalNQueens(self, n: int) -> int:
        full = (1 << n) - 1

        def backtrack(cols, diag1, diag2):
            if cols == full:
                return 1

            count = 0

            # Positions available in this row
            available = full & ~(cols | diag1 | diag2)

            while available:
                # Get the rightmost available position
                bit = available & -available
                available -= bit

                count += backtrack(
                    cols | bit,
                    (diag1 | bit) << 1,
                    (diag2 | bit) >> 1
                )

            return count

        return backtrack(0, 0, 0)