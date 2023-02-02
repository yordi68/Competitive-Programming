# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        slow = head
        fast = head
        slower = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                while slower != slow:
                    slow = slow.next
                    slower = slower.next
                return slower
            
        return None