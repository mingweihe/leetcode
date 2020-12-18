class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
            get a incremental array
            dp[i] may not be the current maximum answer
        """
        dp = []
        pairs = sorted(zip(ages, scores))
        for i, (_, score) in enumerate(pairs):
            dp.append(score)
            for j in xrange(i):
                if score >= pairs[j][1]:
                    dp[-1] = max(dp[-1], score + dp[j])
        return max(dp)
