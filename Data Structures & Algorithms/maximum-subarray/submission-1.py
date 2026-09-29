class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, currSum = nums[0], 0

        for i in range(len(nums)):
            currSum = max(currSum+nums[i], nums[i])
            maxSub = max(currSum, maxSub)
        
        return maxSub