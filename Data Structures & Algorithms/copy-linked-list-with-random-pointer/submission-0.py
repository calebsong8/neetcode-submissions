"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        create a new node
        have to create the next node AND the random node that the node points to to link
        them
        So when you're creating node.next, have to check if its already been created
        Iterate through OG list with a pointer
        """

        cache = {None: None}

        curr = head

        while curr:
            copy = Node(curr.val)
            cache[curr] = copy
            curr = curr.next
        
        curr = head
        
        while curr:
            copy = cache[curr]
            copy.next = cache[curr.next]
            copy.random = cache[curr.random]
            curr = curr.next
        
        return cache[head]