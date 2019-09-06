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
        """
        # Approach 2
        dummy = root
        while dummy:
            node = dummy
            while node:
                if node.left:
                    node.left.next = node.right
                if node.right and node.next:
                    node.right.next = node.next.left
                node = node.next
            dummy = dummy.left
        return root

        # Approach 1
        # if not root: return
        # if root.left:
        #     root.left.next = root.right
        # if root.right and root.next:
        #     root.right.next = root.next.left
        # self.connect(root.left)
        # self.connect(root.right)
        # return root
