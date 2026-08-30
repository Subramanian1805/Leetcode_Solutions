class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        empty = 0
        startRow = 0
        startCol = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    empty += 1

                if grid[r][c] == 1:
                    startRow = r
                    startCol = c

        return self.dfs(grid, startRow, startCol, empty)
    def dfs(self, grid, r, c, empty):
        if (r < 0 or r >= len(grid) or
            c < 0 or c >= len(grid[0]) or
            grid[r][c] == -1):
            return 0
        if grid[r][c] == 2:
            return 1 if empty == 0 else 0
        temp = grid[r][c]
        if grid[r][c] == 0:
            empty -= 1
        grid[r][c] = -1
        paths = (
            self.dfs(grid, r + 1, c, empty) +
            self.dfs(grid, r - 1, c, empty) +
            self.dfs(grid, r, c + 1, empty) +
            self.dfs(grid, r, c - 1, empty)
        )
        grid[r][c] = temp
        return paths