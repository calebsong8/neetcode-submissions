class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dfs(amt):
            if (amt == 0):
                return 0
            if amt not in memo:
                minVal = 1e9

                for coin in coins:
                    if amt-coin >= 0:
                        minVal = min(minVal, 1+dfs(amt-coin))
                
                memo[amt] = minVal
            return memo[amt];

        res = dfs(amount) 
        return -1 if res >= 1e9 else res