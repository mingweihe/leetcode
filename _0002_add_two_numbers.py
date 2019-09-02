class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Approach 1 - recursion
        # if not l1: return l2
        # if not l2: return l1
        # carry, val = divmod(l1.val+l2.val, 10)
        # node = ListNode(val)
        # if carry: l1.next = self.addTwoNumbers(l1.next, ListNode(carry))
        # node.next = self.addTwoNumbers(l1.next, l2.next)
        # return node
        # Approach 2 - iteration ##
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next
