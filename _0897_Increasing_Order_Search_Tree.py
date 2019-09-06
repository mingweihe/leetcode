# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """

    def increasingBST(self, root, tail=None):
        # Approach 2
        if not root: return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res

        # Approach 1
    #     if not root: return root
    #     arr = []
    #     self.helper(arr, root)
    #     cur = head = arr[0]
    #     for i in range(1, len(arr)):
    #         cur.right = arr[i]
    #         cur.left = None
    #         cur = arr[i]
    #     return head
    #
    # def helper(self, arr, node):
    #     if node:
    #         self.helper(arr, node.left)
    #         arr.append(node)
    #         self.helper(arr, node.right)
