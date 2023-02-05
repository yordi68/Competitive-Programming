# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        num1 = ""
        num2 = ""
        
        while cur1:
            num1 = num1 + str(cur1.val)
            cur1 = cur1.next
            
        while cur2:
            num2 = num2 + str(cur2.val)
            cur2 = cur2.next
            
        num1 = num1[::-1]
        num2 = num2[::-1]
        total = str((int(num1) + int(num2)))
        
        newnode = ListNode(0)
        ptr = newnode
        i = len(total) - 1
        
        while i >= 0:
            ptr.next = ListNode(total[i],None)
            ptr = ptr.next
            i -= 1
            
        return newnode.next
            
        
        
        
        
        
