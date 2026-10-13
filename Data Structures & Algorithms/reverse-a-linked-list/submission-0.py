# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        previous = None
        if i is None:
            return None
        while i.next is not None:
            j = i.next
            i.next = previous
            previous = i
            i = j
        i.next = previous
        return i
        
