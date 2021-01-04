# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        ## Approach 2
        def dfs(head, root):
            if not head: return True
            if not root: return False
            return head.val == root.val and (dfs(head.next, root.left) or dfs(head.next, root.right))
        if not head: return True
        if not root: return False
        return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
        ## Approach 1
#         def dfs(node, dq):
#             if not node: return False
#             dq.append(node.val)
#             if len(dq) > L: dq.popleft()
#             if valid(head, dq): return True
#             return dfs(node.left, copy.copy(dq)) or dfs(node.right, copy.copy(dq))
        
#         def valid(node, dq):
#             i = 0
#             while node and i < len(dq):
#                 if node.val != dq[i]: return False
#                 node = node.next
#                 i += 1
#             if node or i != len(dq): return False
#             return True
#         xnode = head
#         L = 0
#         while xnode:
#             L += 1
#             xnode = xnode.next
#         return dfs(root, deque())
