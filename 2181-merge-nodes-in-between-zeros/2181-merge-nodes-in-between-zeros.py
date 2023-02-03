# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        total = 0
        tracker = head
        while fast:
            tracker = slow
            if fast.val == 0:
                slow.val = total
                slow.next = fast
                slow = slow.next
                total = 0
            total += fast.val
            fast = fast.next
        
        tracker.next = None
            
        return head