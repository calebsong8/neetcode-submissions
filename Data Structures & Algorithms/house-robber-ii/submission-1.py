class Solution:
    def rob(self, nums: List[int]) -> int:
        # dynamic programming (can't rob two adjacent houses)
        # adds another decision with the loop

        # changes base case? not recurrency relation i thinK?
        # recurrence: either this house + two down OR next house
        # base: i
        # what's base case to exit loop?
        # introduces more adjacency with first and last
        if len(nums) == 1:
            return nums[0]
                
        cache = [[-1]*2 for _ in range(len(nums))]

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums)-1):
                return 0
            if cache[i][flag] != -1:
                return cache[i][flag]
            
            cache[i][flag] = max(nums[i]+dfs(i+2, flag), dfs(i+1, flag))
            return cache[i][flag]
        
        return max(dfs(0, True), dfs(1, False))