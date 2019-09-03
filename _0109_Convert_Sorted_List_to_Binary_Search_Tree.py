# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        time O(nlog(n))
        space O(n)
        """
        return self.toBST(head, None)

    def toBST(self, head, tail):
        if head == tail: return None
        fast = slow = head
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        node = TreeNode(slow.val)
        node.left = self.toBST(head, slow)
        node.right = self.toBST(slow.next, tail)
        return node
