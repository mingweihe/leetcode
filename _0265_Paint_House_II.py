class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # Approach 3 time O(n*k), space O(1)
        if not costs: return 0
        n, k = len(costs), len(costs[0])
        last_s1, last_s2 = -1, -1
        for i in xrange(n):
            cur1, cur2 = -1, -1
            for j in xrange(k):
                if j == last_s1: costs[i][j] += costs[i-1][last_s2] if i > 0 else 0
                else: costs[i][j] += costs[i-1][last_s1] if i > 0 else 0
                if cur1 < 0 or costs[i][j] < costs[i][cur1]:
                    cur1, cur2 = j, cur1
                elif cur2 < 0 or costs[i][j] < costs[i][cur2]:
                    cur2 = j
            last_s1, last_s2 = cur1, cur2
        return costs[-1][last_s1]

        # Approach 2 time O(n*k), space O(n*k)
        # if not costs: return 0
        # n, k = len(costs), len(costs[0])
        # dp = [[0]*k for _ in xrange(n+1)]
        # last_s1, last_s2 = 0, 0
        # for i in xrange(1, n+1):
        #     cur1, cur2 = -1, -1
        #     for j in xrange(k):
        #         if j == last_s1: dp[i][j] = dp[i-1][last_s2] + costs[i-1][j]
        #         else: dp[i][j] = dp[i-1][last_s1] + costs[i-1][j]
        #         if cur1 < 0 or dp[i][j] < dp[i][cur1]:
        #             cur1, cur2 = j, cur1
        #         elif cur2 < 0 or dp[i][j] < dp[i][cur2]:
        #             cur2 = j
        #     last_s1, last_s2 = cur1, cur2
        # return dp[-1][last_s1]

        # Approach 1 time O(n*k^2), space O(n*k)
        # if not costs: return 0
        # n, k = len(costs), len(costs[0])
        # if k == 1: return sum(zip(*costs)[0])
        # dp = [[0]*k for _ in xrange(n+1)]
        # for i in xrange(1, n+1):
        #     for j in xrange(k):
        #         left = min(dp[i-1][:j] or [float('inf')])
        #         right = min(dp[i-1][j+1:] or [float('inf')])
        #         dp[i][j] = min(left, right) + costs[i-1][j]
        # return min(dp[-1])
