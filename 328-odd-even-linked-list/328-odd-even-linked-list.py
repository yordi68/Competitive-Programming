# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        end = head
        count = 0
        
        while end.next:
            end = end.next
            count += 1
            
        if count % 2 != 0:
            count = (count // 2) + 1
        else:
            count = count // 2
        
        temp = head
        while count:
            end.next = temp.next
            temp.next = temp.next.next
            end.next.next = None
            temp = temp.next
            end = end.next
            count -= 1
        
        return head
        