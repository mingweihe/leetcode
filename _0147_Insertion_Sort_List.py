# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
            time O(n^2)
            space O(1)
        """
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val <= head.next.val:
                head = head.next
            else:
                temp = head.next
                head.next = temp.next
                prev = dummy
                while prev.next.val < temp.val:
                    prev = prev.next
                temp.next = prev.next
                prev.next = temp
        return dummy.next
