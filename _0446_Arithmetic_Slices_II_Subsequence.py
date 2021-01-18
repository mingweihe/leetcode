from collections import defaultdict


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        total = 0
        dp = [defaultdict(int) for _ in xrange(len(A))]
        for i in xrange(len(A)):
            for j in xrange(i):
                diff = A[i]-A[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    total += dp[j][diff]
        return total
