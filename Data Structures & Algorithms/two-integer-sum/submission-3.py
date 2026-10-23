class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stor = {}

        for i, n in enumerate(nums):
            if target - n in stor:
                return [stor[target-n], i]
            stor[n] = i