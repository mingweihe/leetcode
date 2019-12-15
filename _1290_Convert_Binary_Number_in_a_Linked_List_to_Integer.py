# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        # Approach 2
        ans = 0
        while head:
            ans = ans * 2 + head.val
            head = head.next
        return ans

        # Approach 1
        # ans = []
        # while head:
        #     ans.append(str(head.val))
        #     head = head.next
        # return int(''.join(ans), 2)
