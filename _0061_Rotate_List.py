# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        node, L = head, 1
        while node.next:
            node = node.next
            L += 1
        node.next = head
        for i in xrange(L - k % L - 1):
            head = head.next
        res = head.next
        head.next = None
        return res
