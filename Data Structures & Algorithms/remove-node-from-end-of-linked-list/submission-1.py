# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count up all the nodes
        # set index to N - n
        # if the index is 0 (n is the head) return after the head
        # iterate through all the nodes - 1 (for .next.next)
        # compare i + 1 because it starts at zero
        
        total = 0
        curr = head
        while curr:
            total += 1
            curr = curr.next

        removeIndex = total - n
        if removeIndex == 0:
            return head.next
        
        curr = head
        for i in range(total - 1):
            if (i + 1) == removeIndex:
                curr.next = curr.next.next
                break
            curr = curr.next
        
        return head