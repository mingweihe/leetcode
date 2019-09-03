# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        1->2->3->4->5->NULL
        p  c  t
        critical linked list reversion problem
        """
        dummy = node = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in xrange(1, m):
            pre = pre.next
        cur = pre.next
        print cur.val
        for i in xrange(n-m):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
        return dummy.next
