# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # First store root.left, set self.left = self.right, then set self.right = temp
        # Repeat all the way down
        return self.divide(root)
        
    def divide(self, root):
        if not root:
            return None
        
        self.divide(root.left)
        self.divide(root.right)

        return self.conquer(root)
        
    def conquer(self, root):
        temp = root.left
        root.left = root.right
        root.right = temp
        return root