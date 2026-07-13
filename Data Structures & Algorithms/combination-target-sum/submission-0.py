class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # if the total is the same as target add on arr
        # if out of bounds then reutn nothing
        # append and try out cur added then pop it out
        # add one

        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i > len(nums) - 1:
                return
            
            num = nums[i]

            curr.append(num)
            dfs(i, curr, total + num)
            curr.pop()

            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)

        return res