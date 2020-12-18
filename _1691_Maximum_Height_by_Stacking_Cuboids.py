class Solution(object):
    def maxHeight(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        A = [[0, 0, 0]] + sorted(map(sorted, cuboids))
        dp = [0] * len(A)
        for j in xrange(1, len(A)):
            for i in xrange(j):
                if all(A[j][k] >= A[i][k] for k in xrange(3)):
                    dp[j] = max(dp[j], dp[i] + A[j][2])
        return max(dp)
