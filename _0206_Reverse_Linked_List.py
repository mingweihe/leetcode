# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head, p=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Approach 1 separating
        # pre = None
        # while head:
        #     temp = head.next
        #     head.next = pre
        #     pre = head
        #     head = temp
        # return pre

        # Approach 2 connecting
        # dummy = ListNode(0)
        # dummy.next = head
        # while head and head.next:
        #     temp = head.next
        #     head.next = temp.next
        #     temp.next = dummy.next
        #     dummy.next = temp
        # return dummy.next

        # Approach 3 recursion
        if not head: return p
        node = head.next
        head.next = p
        return self.reverseList(node, head)
