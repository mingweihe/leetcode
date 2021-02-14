import itertools


class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## Approach 2
        res = 0
        for _, g in itertools.groupby(s):
            cnt = len([1 for _ in g])
            res += cnt * (cnt + 1)
        return res / 2 % (10**9 + 7)
    
        ## Approach 1
        # dp = []
        # for i, c in enumerate(s):
        #     if not dp or s[i] != s[i-1]:
        #         dp += 1,
        #         continue
        #     dp += dp[i-1] + 1,
        # return sum(dp) % (10**9+7)
