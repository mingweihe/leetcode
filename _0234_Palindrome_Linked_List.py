# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return True
        n, size = head, 0
        while n:
            size += 1
            n = n.next
        n, nH, nS, = head, None, size
        while nS != size // 2:
            n = n.next
            nS -= 1
        nH = n
        n, nH = head, self.reverse(nH)
        while nH:
            if n.val != nH.val: return False
            n = n.next
            nH = nH.next
        return True

    def reverse(self, node, p=None):
        if not node: return p
        t = node.next
        node.next = p
        return self.reverse(t, node)
