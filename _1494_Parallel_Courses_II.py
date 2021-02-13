class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        """
        :type n: int
        :type dependencies: List[List[int]]
        :type k: int
        :rtype: int
            dp + states compression
        """
        # Approach 2, top down, O(n^2 * 2^n)
        @lru_cache(None)
        def dfs(mask, indegree):
            if mask == 0: return 0
            take = []
            for i in range(n):
                if mask & 1 << i and indegree[i] == 0:
                    take.append(i)
            ans = float('inf')
            for courses in combinations(take, min(k, len(take))):
                m, d = mask, list(indegree)
                for c in courses:
                    m ^= 1 << c
                    for nx in graph[c]:
                        d[nx] -= 1
                ans = min(ans, 1 + dfs(m, tuple(d)))
            return ans
            
        graph = defaultdict(list)
        indegree = [0] * n
        for x, y in dependencies:
            graph[x-1].append(y-1)
            indegree[y-1] += 1
        return dfs((1<<n)-1, tuple(indegree))
    
        # Approach 1, bottom up dp, O(2^n * 2^n) TLE
        # dp = [n] * (1<<n)
        # pre_courses = [0] * n
        # prereqs = [0] * (1<<n)
        # bits = [0] * (1<<n)
        # for x, y in dependencies:
        #     pre_courses[y-1] |= 1 << x - 1
        # for state in range(1<<n):
        #     for i in range(n):
        #         if 1 << i & state == 0: continue
        #         prereqs[state] |= pre_courses[i]
        #         bits[state] += 1
        # dp[0] = 0
        # for state in range(1, 1<<n):
        #     sub_state = (state - 1) & state
        #     while sub_state >= 0:
        #         sub_state &= state
        #         if prereqs[state] & sub_state != prereqs[state]:
        #             sub_state -= 1
        #             continue
        #         if bits[state] - bits[sub_state] > k:
        #             sub_state -= 1
        #             continue
        #         dp[state] = min(dp[state], dp[sub_state] + 1)
        #         sub_state -= 1
        # return dp[-1]
