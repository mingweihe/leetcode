# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Approach 2 two pointer
        dummy = ListNode(0)
        fast = slow = dummy
        dummy.next = head
        for i in xrange(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

        # Approach 1 map / dictionary
        # sentinal = ListNode(0)
        # sentinal.next = head
        # dic = {}
        # dic[0] = sentinal
        # no = 0
        # while head:
        #     no += 1
        #     dic[no] = head
        #     head = head.next
        # dic[no-n].next = dic[no-n].next.next
        # return sentinal.next
