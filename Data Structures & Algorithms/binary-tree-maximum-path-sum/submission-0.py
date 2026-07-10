# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # set global variable
        # set leftmax and right max as dfs at first
        # check for negative and set a floor of 0
        # set res value to be the max of itself and the through
        # return the value of the root and the left / right max

        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)

            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        
        dfs(root)

        return res[0]