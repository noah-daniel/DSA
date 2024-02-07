class ListNode:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left


    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -=1
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.left.next, self.left
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next
        

    def addAtTail(self, val: int) -> None:
        node, next, prev = ListNode(val), self.right, self.right.prev
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            node, next, prev = ListNode(val), curr, curr.prev
            prev.next, next.prev = node, node
            node.prev, node.next = prev, next

        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            next, prev = curr.next, curr.prev
            prev.next, next.prev = next, prev

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)