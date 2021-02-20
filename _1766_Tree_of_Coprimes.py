class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        ## Approach 2, conciser, faster, using array
        def dfs(node, depth):
            if node in seen: return
            seen.add(node)
            depthest = -1
            for i in range(1, 51):
                if not path[i]: continue
                if gcd(nums[node], i) == 1 and path[i][-1][1] > depthest:
                    depthest = path[i][-1][1]
                    res[node] = path[i][-1][0]
            path[nums[node]].append((node, depth))
            for nx in graph[node]:
                dfs(nx, depth+1)
            path[nums[node]].pop()
            
        path = [[] for _ in range(51)]
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u] += v,
            graph[v] += u,
        res = [-1] * len(nums)
        seen = set()
        dfs(0, 0)
        return res
        
        ## Approach 1
#         def dfs(node, dic, depth):
#             if node in seen: return
#             seen.add(node)
#             ans = -1
#             ans_dis = float('inf')
#             for k, (dp, anc_i) in dic.items():
#                 if gcd(nums[node], k) == 1 and depth - dp < ans_dis:
#                     ans_dis = depth - dp
#                     ans = anc_i
#             res[node] = ans
#             dic[nums[node]] = (depth, node)
#             for nx in graph[node]:
#                 if nx in seen: continue
#                 new_dic = copy.copy(dic)
#                 dfs(nx, new_dic, depth + 1)
            
#         graph = defaultdict(list)
#         for u, v in edges:
#             graph[u] += v,
#             graph[v] += u,
        
#         n = len(nums)  
#         res = [-1] * n
#         seen = set()
#         dfs(0, {}, 0)
#         return res
