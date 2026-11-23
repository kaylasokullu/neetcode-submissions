# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        previous = head 
        current = head.next 
        while current is not None:
            use = current.next 
            current.next = previous 
            if previous is head: #deals with first one
                previous.next = None
            previous = current
            current = use
        return previous