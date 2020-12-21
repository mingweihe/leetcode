import math

## Approach 2
class TreeAncestor(object):

    def __init__(self, n, parent):
        """
        :type n: int
        :type parent: List[int]
        """
        self.steps = int(math.log10(n)/math.log10(2))
        A = {i: x for i, x in enumerate(parent)}
        self.jump = [A]
        for _ in xrange(self.steps):
            B = {}
            for i in A:
                if A[i] in A:
                    B[i] = A[A[i]]
            self.jump += B,
            A = B

    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """
        steps = self.steps
        while k and node != -1:
            if k >= 1 << steps:
                node = self.jump[steps].get(node, -1)
                k -= 1 << steps
            steps -= 1
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)

## Approach 1
# import lru_cache


# class TreeAncestor:

#     def __init__(self, n: int, parent: List[int]):
#         self.parent = parent

#     @lru_cache(None)
#     def dp(self, node: int, k: int) -> int:
#         if node == -1: return -1
#         if k == 0: return node
#         if node == 0 and k != 0: return -1
#         if k == 1: return self.parent[node]
#         return self.dp(self.dp(node, k >> 1), k >> 1)
    
#     def getKthAncestor(self, node: int, k: int) -> int:
#         if k == 0: return node
#         if node == 0 and k != 0: return -1
#         low_bit = k & -k
#         rest_k = k - low_bit
#         p_low_bit = self.dp(node, low_bit)
#         if p_low_bit == -1: return -1
#         return self.getKthAncestor(p_low_bit, rest_k)


# # Your TreeAncestor object will be instantiated and called as such:
# # obj = TreeAncestor(n, parent)
# # param_1 = obj.getKthAncestor(node,k)