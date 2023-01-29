# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode(0)
        greater = ListNode(0)
        ptr_l = less
        ptr_g = greater
        
        while head != None:
            
            if head.val < x:
                ptr_l.next = head
                ptr_l = ptr_l.next

            else:
                ptr_g.next = head
                ptr_g = ptr_g.next

            head = head.next
            
        ptr_g.next = None
        ptr_l.next = greater.next
            
        return less.next
        
        