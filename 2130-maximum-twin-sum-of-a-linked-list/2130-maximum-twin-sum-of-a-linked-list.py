# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Finding the middle value
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reversing second half of the linked list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        # doing the main problem
        left , right = head , prev
        maxSum = 0
        while right:
            maxSum = max(maxSum , left.val + right.val)
            left = left.next
            right = right.next
        return maxSum
        
        
        