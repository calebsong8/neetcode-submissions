class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # compare values
        # how do we know if target is in left / right side?
        # if statement for whether l to m is increasing zone
        # checks if target isn't in that increasing zone, in which case changes values accordingly
        # vice versa
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2

            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            
        return -1

