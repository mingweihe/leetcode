# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Approach 2
        if not head: return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast: return True
        return False

        # Approach 1
        # cH = head
        # while cH:
        #     if cH.val == 'passed': return True
        #     cH.val = 'passed'
        #     cH = cH.next
        # return False
