class Solution:
    def climbStairs(self, n: int) -> int:
        # new pattern + trigger
        # recursion?
        # dynamic programming + memoization

        cache = [0] * n

        def dfs(num):
            if num >= n:
                return num == n
            
            if cache[num] != 0:
                return cache[num]
            cache[num] = dfs(num+1) + dfs(num+2)
            return cache[num]

        return dfs(0)

        