# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        self.maxValue = float("-inf")
        
        def traverse(node):
            if not node:
                return node
            
            node.next = traverse(node.next)
            
            self.maxValue = max(self.maxValue,node.val)
            
            if self.maxValue > node.val:
                return node.next
            
            return node
        
        return traverse(head)

            
        
