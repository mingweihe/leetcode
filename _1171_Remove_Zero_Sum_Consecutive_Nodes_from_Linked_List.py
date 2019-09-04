# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = node = ListNode(0)
        dummy.next = head
        m = {}
        summ = 0
        while node:
            summ += node.val
            m.setdefault(summ, node).next = node = node.next
        return dummy.next
