class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # diagonal does not matter for island existence
        # count number of unique islands
        # return max?

        # backtracking approach:
        # mark every visited cell with a !
        # how to track unique islands?
        # all surrounding cells of islands are either 0 or None
        # maybe don't even have to backtrack

        islandCount = 0
        rows, cols = len(grid), len(grid[0])

        def explore(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '!' or grid[r][c] == "0" or grid[r][c] == None:
                return
            grid[r][c] = '!'
            explore(r+1, c)
            explore(r-1, c)
            explore(r, c+1)
            explore(r, c-1)
            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islandCount += 1
                    explore(r, c)
        
        return islandCount
            