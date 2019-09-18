# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # Approach 2 time O(k*log(n))
        res, pred, succ = [], [], []
        self.init_pred(root, target, pred)
        self.init_succ(root, target, succ)
        if pred and succ and pred[-1].val == succ[-1].val:
            self.helper(pred, False)
        while k:
            if not succ:
                res.append(self.helper(pred, False))
            elif not pred:
                res.append(self.helper(succ, True))
            else:
                succ_diff = abs(succ[-1].val - target)
                pred_diff = abs(pred[-1].val - target)
                if succ_diff < pred_diff:
                    res.append(self.helper(succ, True))
                else:
                    res.append(self.helper(pred, False))
            k -= 1
        return res

    def helper(self, stack, is_succ):
        node = stack.pop()
        res = node.val
        if is_succ:
            node = node.right
        else:
            node = node.left
        while node:
            stack.append(node)
            if is_succ:
                node = node.left
            else:
                node = node.right
        return res

    def init_pred(self, node, target, pred):
        while node:
            if node.val == target:
                pred.append(node)
                break
            elif node.val < target:
                pred.append(node)
                node = node.right
            else:
                node = node.left

    def init_succ(self, node, target, succ):
        while node:
            if node.val == target:
                succ.append(node)
                break
            elif node.val > target:
                succ.append(node)
                node = node.left
            else:
                node = node.right

        # Approach 1 time O(n)
        # def dfs(ans, node):
        #     if node is None: return
        #     dfs(ans, node.left)
        #     if len(ans) == k:
        #         if ans and abs(ans[0]-target) > abs(node.val-target):
        #             ans.pop(0)
        #         else: return
        #     ans.append(node.val)
        #     dfs(ans, node.right)
        # res = []
        # dfs(res, root)
        # return res
