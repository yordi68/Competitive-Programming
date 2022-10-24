# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        # find the middlle index
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse secong half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        # check palindrome
        l,r = head,prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True