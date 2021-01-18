from collections import defaultdict


class Solution(object):
    def mostSimilar(self, n, roads, names, targetPath):
        """
        :type n: int
        :type roads: List[List[int]]
        :type names: List[str]
        :type targetPath: List[str]
        :rtype: List[int]
        """
        ## Approach 3, bottom-up DP
        m = len(targetPath)
        dp = [[float('inf')] * n for _ in xrange(m+1)]
        for i in xrange(n):
            dp[0][i] = 0
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        parents = [[-1] * n for _ in xrange(m+1)]
        for i in xrange(1, m+1):
            for v in xrange(n):
                prev_min = float('inf')
                for u in graph[v]:
                    if dp[i-1][u] < prev_min:
                        prev_min = dp[i-1][u]
                        parents[i][v] = u
                dp[i][v] = prev_min + (1 if names[v] != targetPath[i-1] else 0)
        min_dis, end_city = float('inf'), -1
        for v in xrange(n):
            if dp[m][v] < min_dis:
                min_dis = dp[m][v]
                end_city = v
        res = [-1] * (m - 1) + [end_city]
        for i in xrange(m-2, -1, -1):
            res[i] = parents[i+2][res[i+1]]
        return res
        
        ## Approach 2, top-down DP
#         def dfs(i, v):
#             if i == -1: return 0
#             if (i, v) in cache: return cache[i, v]
#             ans = float('inf')
#             for u in graph[v]:
#                 cur_min = dfs(i-1, u)
#                 if cur_min < ans:
#                     ans = cur_min
#                     parent_nodes[i][v] = u
#             ans += names[v] != targetPath[i]
#             cache[i, v] = ans
#             return ans
        
#         def get_result(v):
#             ans = [0] * (m-1) + [v]
#             for i in xrange(m-2, -1, -1):
#                 ans[i] = parent_nodes[i+1][ans[i+1]]
#             return ans
            
#         graph = defaultdict(list)
#         for u, v in roads:
#             graph[u] += v,
#             graph[v] += u,
    
#         cache = dict()
#         min_dis = float('inf')
#         m = len(targetPath)
#         res = []
#         parent_nodes = [[0]*n for _ in xrange(m)]
#         for i in xrange(n):
#             cur_dis = dfs(m-1, i)
#             if cur_dis < min_dis:
#                 min_dis = cur_dis
#                 res = get_result(i)
#         return res

        ## Approach 1, brute force, O(n^n), TLE
#         def dfs(i, j, dis, cur):
#             if i == len(targetPath):
#                 if dis < self.min_dis:
#                     self.res = cur[:]
#                     self.min_dis = dis
#                 return
#             for next_city in graph[j]:
#                 cur.append(next_city)
#                 dfs(i+1, next_city, dis + (names[next_city] != targetPath[i]), cur)
#                 cur.pop()
        
#         graph = defaultdict(list)
#         for u, v in roads:
#             graph[u] += v,
#             graph[v] += u,
#         self.min_dis = float('inf')
#         self.res = []
#         for i in xrange(n):
#             dfs(1, i, targetPath[0] != names[i], [i])
#         return self.res
