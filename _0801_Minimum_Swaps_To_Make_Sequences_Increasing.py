class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        dp = [[float('inf'), float('inf')] for _ in xrange(n)]
        dp[0] = [0, 1]
        for i in xrange(1, n):
            pa, pb = A[i-1], B[i-1]
            a, b = A[i], B[i]
            if pa < a and pb < b:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1] + 1
            if pb < a and pa < b:
                dp[i][0] = min(dp[i][0], dp[i-1][1])
                dp[i][1] = min(dp[i][1], dp[i-1][0] + 1)
        return min(dp[-1])
