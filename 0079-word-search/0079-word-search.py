class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):

                if self.dfs(board, word, i, j, 0):
                    return True

        return False

    def dfs(self, board, word, row, col, index):

        if index == len(word):
            return True

        if (row < 0 or row >= len(board) or
            col < 0 or col >= len(board[0])):
            return False

        if board[row][col] != word[index]:
            return False

        temp = board[row][col]
        board[row][col] = '#'

        found = (
            self.dfs(board, word, row + 1, col, index + 1) or  
            self.dfs(board, word, row - 1, col, index + 1) or
            self.dfs(board, word, row, col + 1, index + 1) or 
            self.dfs(board, word, row, col - 1, index + 1)     
        )

        board[row][col] = temp

        return found
