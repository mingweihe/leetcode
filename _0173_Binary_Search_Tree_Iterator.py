# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.array = []
        self.index = 0
        if not root: return
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            self.array.append(node.val)
            node = node.right

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        next_val = self.array[self.index]
        self.index += 1
        return next_val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.index == len(self.array):
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
