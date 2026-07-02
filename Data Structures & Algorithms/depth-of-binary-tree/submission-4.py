# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # initialize double-ended queue
        # if there's a root, append the root to queue
        # set level to be zero
        # while queue isn't empty
        # for each i in a given level (from each adding session) pop the first node
        # then append their babies if they exist
        # add one to level once you're done

        q = deque()

        level = 0

        if root:
            q.append(root)
        
        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        
        return level