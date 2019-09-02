# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        l1 = dummy
        l2 = head
        while l2 and l2.next:
            node = l2.next.next
            l1.next = l2.next
            l2.next.next = l2
            l2.next = node
            l1 = l2
            l2 = node
        return dummy.next
