# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        def compare(list1, list2):
            nonlocal dummy
            if not list1 and not list2:
                return
            if not list1:
                dummy.next = list2
                dummy = dummy.next
                return
            if not list2:
                dummy.next = list1
                dummy = dummy.next
                return

            if list1.val > list2.val:
                tmp = list2.next
                list2.next = None
                dummy.next = list2
                dummy = dummy.next
                compare(list1,tmp)

            else:
                tmp = list1.next
                list1.next = None
                dummy.next = list1
                dummy = dummy.next
                compare(tmp,list2)

        compare(list1,list2)

        return cur.next