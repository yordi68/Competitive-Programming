# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dummy1 = headA
        dummy2 = headB
        
        while dummy1 != dummy2:
            dummy1 = headB if not dummy1 else dummy1.next
            dummy2 = headA if not dummy2 else dummy2.next
            
        return dummy1
        