class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
            Union-find algorithm with Disjoint set data structure
            find turns O(1) from O(h) by using path compression
            So time complexity is O(V+E)
            V is the first line building the roots
            E is traversing all the edges
        """
        roots = range(n)

        def find(idx):
            if roots[idx] != idx:
                # path compression
                roots[idx] = find(roots[idx])
            return roots[idx]
        for x, y in edges:
            roots[find(x)] = find(y)
        return len(set(map(find, roots)))
