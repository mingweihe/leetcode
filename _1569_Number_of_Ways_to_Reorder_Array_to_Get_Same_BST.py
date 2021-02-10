class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = Node(nums[0])
        def insert(node, val):
            if node.val > val:
                if not node.left: node.left = Node(val)
                else: insert(node.left, val)
            else:
                if not node.right:  node.right = Node(val)
                else: insert(node.right, val)
                
        for x in nums[1:]:
            insert(root, x)
        
        def comb(m, n):
            res = 1
            for num in xrange(n):
                res *= m
                m -= 1
            for num in xrange(2, n+1):
                res /= num
            return res
        
        def count(node):
            if not node: return 0, 1
            n_left, o_left = count(node.left)
            n_right, o_right = count(node.right)
            n_node = n_left + n_right + 1
            n_order = comb(n_left + n_right, n_left) * o_left * o_right
            return n_node, n_order
        
        return (count(root)[1] - 1) % (10**9+7)
