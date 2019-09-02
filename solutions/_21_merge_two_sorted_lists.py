# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Method 1 recursion
        if not l1: return l2
        if not l2: return l1

        if l1.val > l2.val:
            head = ListNode(l2.val)
            head.next = self.mergeTwoLists(l1, l2.next)
        else:
            head = ListNode(l1.val)
            head.next = self.mergeTwoLists(l1.next, l2)
        return head

        # Method 2 iteration
        # if l1 is None: return l2
        # if l2 is None: return l1
        # if l1.val >= l2.val:
        #     head = ListNode(l2.val)
        #     l2 = l2.next
        # else:
        #     head = ListNode(l1.val)
        #     l1 = l1.next
        # node = head
        # while l1 and l2:
        #     if l1.val >= l2.val:
        #         node.next = l2
        #         node = l2
        #         l2 = l2.next
        #     else:
        #         node.next = l1
        #         node = l1
        #         l1 = l1.next
        # node.next = l1 or l2
        # return head
