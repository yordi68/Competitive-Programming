class MyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):
    def __init__(self):

        self.head = None
        self.length = 0

    def get(self, index: int) -> int:

        if index < 0 or index >= self.length:
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:

        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:

        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:

        if index > self.length:
            return
        current = self.head
        if index <= 0:
            self.head=MyNode(val, self.head)
        else:
            for i in range(index - 1):
                current = current.next
            current.next=MyNode(val, current.next)
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.length:
            return
        current = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.length -= 1