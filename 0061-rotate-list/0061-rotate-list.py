# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = head
        fast = head
        ptr = head
        if not head:
            return head
        
        length = 0
        
        while ptr:
            ptr = ptr.next
            length += 1
        
        k = k % length
        
        if length < 2 or k == 0:
            return head
        
        for i in range(k):
            fast = fast.next
                   
        while fast.next:

            slow = slow.next
            fast = fast.next
        newhead = slow.next
        
        slow.next = None
        fast.next = head
        
        return newhead
        