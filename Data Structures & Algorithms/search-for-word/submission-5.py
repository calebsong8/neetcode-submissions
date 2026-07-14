class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # define rows and cols
        # make dfs be indices of row, col, and word char
        # account for if i is the length of the word
        # accout for false cases of the row or cols being out of bounds or unmatched word
        # or #
        # set board as hashtag
        # try all horizontal and vert cases with a hashtag
        # revert back
        # try for every value of board
        # common pattern: restore cell after backtracking

        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i] or board[r][c] == '#'):
                return False
            
            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or 
                    dfs(r, c + 1, i + 1) or 
                    dfs(r, c - 1, i + 1))
            board[r][c] = word[i]

            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False