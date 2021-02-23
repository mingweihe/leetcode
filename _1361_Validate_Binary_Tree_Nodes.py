class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        def dfs(node):
            if node == -1: return
            if node in seen:
                self.res = False
                return
            seen.add(node)
            dfs(leftChild[node])
            dfs(rightChild[node])
        
        self.res = True
        seen = set()
        roots = set(range(n))
        for i in xrange(n):
            if leftChild[i] != -1:
                roots.discard(leftChild[i])
            if rightChild[i] != -1:
                roots.discard(rightChild[i])
        
        if len(roots) != 1: return False
        dfs(roots.pop())
        return self.res and len(seen) == n
