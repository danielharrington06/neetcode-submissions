# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using the one and two step appoach
        # one pointer moves one step at a time and the other goes twice at a time

        one = two = head
        if head == None:
            return False

        while one and two:
            one = one.next
            two = two.next
            if two == None:
                return False
            two = two.next
            if one == two:
                return True
        return False