class MyLinkedList(object):
    class Node:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.tail = None
        self.size = 0

    def _print(self):
        res = ""
        node = self.tail
        while node:
            res += "<-" + str(node.val)
            node = node.prev
        print(res)

    def _get_node(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        idx = 0
        if index <= self.size / 2:
            node = self.head
            while idx != index:
                node = node.next
                idx += 1
        else:
            idx = self.size - 1
            node = self.tail
            while idx != index:
                node = node.prev
                idx -= 1
        return node

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        node = self._get_node(index)
        if not node or node == -1: return -1
        return node.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new_head = self.Node(val)
        if self.size == 0:
            self.head = self.tail = new_head
        else:
            self.head.prev = new_head
            new_head.next = self.head
            self.head = new_head
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        new_tail = self.Node(val)
        if self.size == 0:
            self.head = self.tail = new_tail
        else:
            self.tail.next = new_tail
            new_tail.prev = self.tail
            self.tail = new_tail
        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        pre_node = self._get_node(index - 1)
        new_node = self.Node(val)
        new_node.next = pre_node.next
        if pre_node.next:
            pre_node.next.prev = new_node
        pre_node.next = new_node
        new_node.prev = pre_node
        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        target = self._get_node(index)
        if target == -1: return
        prev = target.prev
        ne = target.next
        if prev and ne:
            prev.next = ne
            ne.prev = prev
            self.size -= 1
            return
        if self.size == 1:
            self.head = self.tail = None
        else:
            if prev is None:
                ne.prev = prev
                self.head = ne
            if ne is None:
                prev.next = ne
                self.tail = prev
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
