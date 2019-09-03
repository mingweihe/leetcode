# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small_head, big_head = ListNode(0), ListNode(0)
        small, big = small_head, big_head
        while head:
            node = ListNode(head.val)
            if head.val < x:
                small.next = node
                small = small.next
            else:
                big.next = node
                big = big.next
            head = head.next
        small.next = big_head.next
        return small_head.next
