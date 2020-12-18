class Solution(object):
    def kthSmallestPath(self, destination, k):
        """
        :type destination: List[int]
        :type k: int
        :rtype: str
        """
        m, n = destination
        dp = [[1] * (n+1) for _ in xrange(m+1)]
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        res = ''
        while m != 0 and n != 0:
            if dp[m][n-1] >= k:
                n -= 1
                res += 'H'
            else:
                k -= dp[m][n-1]
                m -= 1
                res += 'V'
        res += 'H' * n + 'V' * m
        return res
