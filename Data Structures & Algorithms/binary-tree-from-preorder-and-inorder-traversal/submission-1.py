# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # how do you know if a root is left, right, or the root?
        # compare the preorder and inorder values at given indices / use pointers
        # reconstruct with node.left = x and node.right = y
        # wrap value in tree node to set equal to
        # make general case - use logical reasoning for tautology not case by case
        # first value of preorder is always root
        # maybe build from bottom up
        # fill in the gaps of knowledge from one traversal with the other

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root