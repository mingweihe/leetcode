class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        def dfs(x):
            if x in ans: return ans[x]
            if vis[x]: return False
            vis[x] = True
            ok = True
            for nx in graph[x]:
                ok &= dfs(nx)
            vis[x] = False
            ans[x] = ok
            return ok
        ans = {}
        vis = [False] * len(graph)
        for i in xrange(len(graph)): dfs(i)
        return [i for i in xrange(len(graph)) if ans[i]]
