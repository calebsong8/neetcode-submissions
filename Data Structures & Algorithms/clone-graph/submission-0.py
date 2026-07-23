"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # is this not just iterating through and making a basic copy with maybe some dfs involved
        # neighbors are a list of nodes
        # wait its deadass just dfs or bfs woohoo i found the pattern!
        # seperate the queue popping the node and the making the copy behaviors
        if not node:
            return None
        
        ogToCopy = {}
        ogToCopy[node] = Node(node.val)

        q = deque([node])
        
        while q:
            curr = q.popleft()
            neighbors = curr.neighbors
            for neighbor in neighbors:
                if neighbor not in ogToCopy:
                    ogToCopy[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                ogToCopy[curr].neighbors.append(ogToCopy[neighbor])
        
        return ogToCopy[node]

                

        


        