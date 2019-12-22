# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd_head = odd_tail = ListNode(0)
        even_head = even_tail = ListNode(0)
        idx = 1
        while head:
            if idx & 1:
                odd_tail.next = head
                odd_tail = odd_tail.next
            else:
                even_tail.next = head
                even_tail = even_tail.next
            head = head.next
            idx += 1
        even_tail.next = None
        odd_tail.next = even_head.next
        return odd_head.next
