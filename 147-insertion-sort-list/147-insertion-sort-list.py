# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        
        prev = head
        cur = head.next
        while cur:
            if cur.val >= prev.val:
                prev = cur
                cur = cur.next
                continue
            
            tmp = temp
            while cur.val >= tmp.next.val:
                tmp = tmp.next
            
            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next
            
        return temp.next
            