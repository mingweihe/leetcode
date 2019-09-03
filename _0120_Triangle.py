class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        bottom-up dp similar to the theory of merge sorting
        bottom-up can avoid covering previous needed dp value
        sometime, we have to consider problem from diffrent perspectives / views
        """
        L = len(triangle)
        dp = [0]*(L+1)
        for i in xrange(L-1, -1, -1):
            for j in xrange(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
