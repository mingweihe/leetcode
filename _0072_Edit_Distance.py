class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        "horse" -> "ros"
       [[0, 1, 2, 3],
        [1, 1, 2, 3],
        [2, 2, 1, 2],
        [3, 2, 2, 2],
        [4, 3, 3, 2],
        [5, 4, 4, 3]]
        time  O(m * n)
        space O(m * n)
        """
        L1, L2 = len(word1)+1, len(word2)+1
        dp = [[0]*L2 for _ in xrange(L1)]
        for i in xrange(L1):
            dp[i][0] = i
        for i in xrange(L2):
            dp[0][i] = i
        for i in xrange(1, L1):
            for j in xrange(1, L2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        return dp[-1][-1]
