class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(node, path, ans):
            if node == len(graph)-1:
                ans += path,
                return
            for nx in graph[node]:
                dfs(nx, path+[nx], ans)
        ans = []
        dfs(0, [0], ans)
        return ans
