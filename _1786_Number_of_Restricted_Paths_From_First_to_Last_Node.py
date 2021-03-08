class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u] += (v, w),
            graph[v] += (u, w),
        
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        hq = [[0, n]]
        # dijkstra
        while hq:
            d, x = heappop(hq)
            # ignore previously added entry with longer distance
            if d != dist[x]: continue
            for nx, w in graph[x]:
                if dist[nx] <= d + w: continue
                dist[nx] = d + w
                heappush(hq, [d + w, nx])
                
        @lru_cache(None)
        def dfs(node):
            if node == n: return 1
            ans = 0
            for nx, w in graph[node]:
                if dist[node] <= dist[nx]: continue
                ans += dfs(nx)
            return ans
        
        return dfs(1) % (10**9 + 7)
