from bisect import bisect_left


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        sorting + find the longest increasing sequence
        """
        # Approach 2 O(n*logn)
        if not envelopes: return 0
        dp = []
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        A = zip(*envelopes)[1]
        for x in A:
            idx = bisect_left(dp, x)
            if idx >= len(dp): dp += x,
            else: dp[idx] = x
        return len(dp)
        
        # Approach 1 O(n^2)
        # envelopes.sort(key=lambda x: (x[0], -x[1]))
        # N = len(envelopes)
        # dp = [1] * N
        # res = 0
        # for i in xrange(N):
        #     for j in xrange(i):
        #         if envelopes[i][1] > envelopes[j][1]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        #     res = max(res, dp[i])
        # return res
