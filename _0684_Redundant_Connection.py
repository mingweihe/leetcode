class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
            find the answer in the process of constructing the structural data
        """
        def find(x):
            if roots[x] != x:
                roots[x] = find(roots[x])
            return roots[x]

        roots = range(len(edges)+1)
        ans = None
        for u, v in edges:
            uu = find(u)
            vv = find(v)
            if uu == vv: ans = [u, v]
            else: roots[uu] = vv
        return ans
