# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val, p = None):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return None
        if head.val != val:
            head.next = self.removeElements(head.next, val, head)
            return head
        return self.removeElements(head.next, val, p)
