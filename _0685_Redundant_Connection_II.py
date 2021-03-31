class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # union find -> find the cycle
        def find(x):
            if roots[x] != x:
                roots[x] = find(roots[x])
            return roots[x]
        parents = [0] * (len(edges) + 1)
        ans1 = ans2 = None
        for i, (u, v) in enumerate(edges):
            if parents[v]:
                ans1 = [parents[v], v]
                ans2 = [u, v]
                edges[i] = [-1, -1]
            parents[v] = u
        roots = range(len(edges)+1)
        for u, v in edges:
            if u == -1: continue
            uu, vv = find(u), find(v)
            #  cycle case
            if uu == vv:
                # return edge coming late and having two parents
                if not ans1: return [u, v]
                # return the edge with node having two parents and in the cycle
                else: return ans1
            else: roots[uu] = vv
        # no cycle case 1: because cutting nodes in ans2 edge 
        # no cycle case 2: truly no cycle, edge coming late is the answer
        return ans2
