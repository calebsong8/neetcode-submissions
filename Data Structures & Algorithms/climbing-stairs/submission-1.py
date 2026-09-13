class Solution:
    def climbStairs(self, n: int) -> int:
        # new pattern + trigger
        # recursion?
        # dynamic programming + memoization

        cache = [0] * n

        def dfs(num):
            if num == n:
                return 1
            if num > n:
                return 0
            
            if cache[num] != 0:
                return cache[num]
            res = dfs(num+1) + dfs(num+2)
            cache[num] = res
            return res

        return dfs(0)
