class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res, l, r = 0, 0, len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (l-r)
            res = min(area, res)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return abs(res)