class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, currSum = nums[0], 0

        for i in range(len(nums)):
            if currSum < 0:
                currSum = 0
            currSum += nums[i]
            maxSub = max(currSum, maxSub)
        
        return maxSub