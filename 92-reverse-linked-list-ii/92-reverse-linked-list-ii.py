# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode(1453)
        dummy_node.next = head
        cur = head
        prev = dummy_node
        
        count = 1
        while cur and count < left:
            prev = cur
            cur = cur.next
            count += 1
            
        nextt = cur
        
        reversed_head = prev
        right_next = cur
            
        while left <= right and cur:
            nextt = nextt.next
            cur.next = prev
            prev = cur
            cur = nextt
            left += 1

        right_next.next = nextt
        reversed_head.next = prev
        
        return dummy_node.next
