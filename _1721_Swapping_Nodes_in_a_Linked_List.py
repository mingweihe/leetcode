# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        ## Approach 2
        n1, n2, node = None, None, head
        while node:
            k -= 1
            if n2: n2 = n2.next
            if k == 0:
                n1 = node
                n2 = head
            node = node.next
        n1.val, n2.val = n2.val, n1.val
        return head

        ## Approach 1
        # node = head
        # A = []
        # while node:
        #     A += node,
        #     node = node.next
        # A[k-1].val, A[len(A)-k].val = A[len(A)-k].val, A[k-1].val
        # return head
