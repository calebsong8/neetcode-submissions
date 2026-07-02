# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # iterate through all the nodes and if a match is found return true
        # else after iteration return false
        # how to find match?
        # maybe iterate through each value, check if the node value matches the subroots, then
        # check if they're equal?

        stack = [root]

        while stack:
            for _ in range(len(stack)):
                node = stack.pop()

                if node.val == subRoot.val:
                    if self.valueMatch(node, subRoot):
                        return True

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        
        return False

    def valueMatch(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.valueMatch(p.left, q.left) and self.valueMatch(p.right, q.right)
        else:
            return False
