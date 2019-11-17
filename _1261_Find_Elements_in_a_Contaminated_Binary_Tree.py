# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # Approach 2
        self.seen = set()
        if not root: return
        root.val = 0
        self.seen.add(0)

        def helper(node, val):
            if not node: return
            node.val = val
            self.seen.add(val)
            helper(node.left, val * 2 + 1)
            helper(node.right, val * 2 + 2)

        helper(root.left, 1)
        helper(root.right, 2)

        # Approach 1
        # if not root: return
        # root.val = 0
        # def helper(node, val):
        #     if not node: return
        #     node.val = val
        #     helper(node.left, val*2+1)
        #     helper(node.right, val*2+2)
        # helper(root.left, 1)
        # helper(root.right, 2)
        # self.tree = []
        # queue = collections.deque([root])
        # while queue:
        #     for _ in xrange(len(queue)):
        #         node = queue.popleft()
        #         self.tree.append(node.val)
        #         if node.left: queue.append(node.left)
        #         if node.right: queue.append(node.right)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        # Approach 2
        return target in self.seen
        # Approach 1
        # idx = bisect.bisect(self.tree, target) - 1
        # return self.tree[idx] == target

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
