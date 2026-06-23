class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search
        # Given condition move points to half of current length
        # Objective: find out which half the min value is everytime
        
        l, r = 0, len(nums) - 1

        while l < r:
            half = l + (r - l) // 2
            if nums[half] < nums[r]:
                r = half
            else:
                l = half + 1
        
        return nums[l]
