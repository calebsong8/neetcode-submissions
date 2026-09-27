class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # base case: reach grid[m-1][n-1] return 0, if you hit a wall return 
        # recursion: go right or down
        # condition: stay in bounds (0, m-1, n-1)
        # cache: trues? every time true is hit increment up by one?

        cache = [[-1 for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            if i == m - 1 and j == n - 1:
                return 1
            cache[i][j] = dfs(i+1, j) + dfs(i, j+1)
            return cache[i][j]

        return dfs(0,0)