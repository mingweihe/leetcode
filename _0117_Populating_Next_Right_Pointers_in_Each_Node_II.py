# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        head, cur, pre node analysis
        """
        cur = root
        head = pre = None
        while cur:
            while cur:
                if cur.left:
                    if pre: pre.next = cur.left
                    else: head = cur.left
                    pre = cur.left
                if cur.right:
                    if pre: pre.next = cur.right
                    else: head = cur.right
                    pre = cur.right
                cur = cur.next
            cur = head
            head = pre = None
        return root
