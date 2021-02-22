class Solution(object):
    def maxSizeSlices(self, slices):
        """
        :type slices: List[int]
        :rtype: int
            similar to house robber II
        """
        def get_max(slices):
            m = len(slices)
            dp = [[0] * (n+1) for _ in xrange(m+1)]
            for i in xrange(1, m+1):
                for j in xrange(1, n+1):
                    dp[i][j] = max(dp[i-1][j], slices[i-1] + (dp[i-2][j-1] if i > 1 else 0))
            return dp[m][n]
        
        n = len(slices) / 3
        return max(get_max(slices[1:]), get_max(slices[:-1]))
