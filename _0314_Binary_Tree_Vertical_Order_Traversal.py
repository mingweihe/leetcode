import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Approach 2, min, max variables, time O(n)
        if not root: return []
        dic, queue = collections.defaultdict(list), [(root, 0)]
        min_ind = max_ind = 0
        for node, i in queue:
            if node:
                dic[i].append(node.val)
                queue.append((node.left, i - 1))
                queue.append((node.right, i + 1))
                min_ind, max_ind = min(min_ind, i), max(max_ind, i)
        return [dic[i] for i in xrange(min_ind, max_ind + 1)]

        # Approach 1, time O(n*log(n))
        # dic, queue = collections.defaultdict(list), [(root, 0)]
        # for node, i in queue:
        #     if node:
        #         dic[i].append(node.val)
        #         queue.append((node.left, i-1))
        #         queue.append((node.right, i+1))
        # return [dic[i] for i in sorted(dic)]
