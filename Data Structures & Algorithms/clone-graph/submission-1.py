"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS
        ogToClone = {}

        def dfs(node):
            if node in ogToClone:
                return ogToClone[node]
            copy = Node()
            copy.val = node.val
            
            ogToClone[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
        
        return dfs(node) if node else None
