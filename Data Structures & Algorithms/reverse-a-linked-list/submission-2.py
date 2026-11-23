# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#recursive solution 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: #if empty, return nule 
            return None
        newHead = head #new head copy 
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head #getting the previous head.next to point towards it's head instead. Example head = B. head.next = C. C.next = B
        head.next = None #cuts the loop from B.next = C to b.next to nothing
        return newHead #return the pointer 