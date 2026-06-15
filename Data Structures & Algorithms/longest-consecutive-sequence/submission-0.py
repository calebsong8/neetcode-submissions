class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        res = set()

        for num in nums:
            res.add(num)

        maxCount = 0

        for num in res:
            curr = num
            count = 1
            while curr - 1 in res:
                count += 1
                curr -= 1
            curr = num
            while curr + 1 in res:
                count += 1
                curr += 1
            if count > maxCount:
                maxCount = count
        
        return maxCount