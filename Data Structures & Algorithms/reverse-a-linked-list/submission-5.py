# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev = None
        curr = head
        nxt = curr.next
        head.next = None
        while nxt and nxt.next != None:
            prev = curr
            curr = nxt

            nxt = curr.next
            curr.next = prev
        if nxt is None:
            return curr
        nxt.next = curr

        return nxt