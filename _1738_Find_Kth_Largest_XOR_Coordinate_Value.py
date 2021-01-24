class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in xrange(m+1)]
        res = []
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                dp[i][j] = dp[i-1][j] ^ dp[i][j-1] ^ dp[i-1][j-1] ^ matrix[i-1][j-1]
                res += dp[i][j],
        return sorted(res, reverse=True)[k-1]
