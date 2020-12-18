class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## Approach 3
        dp = [[0]*2 for _ in xrange(len(s)+1)]
        for i in xrange(1, len(s)+1):
            if s[i-1] == 'b':
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = dp[i-1][1]
            else:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = min(dp[i-1][1]+1, dp[i][0])
        return dp[-1][1]
                
        ## Approach 2
        # a, b = 0, 0
        # for c in s:
        #     if c == 'b': a += 1
        #     else: b = min(a, b+1)
        # return b
        
        ## Approach 1
        # dp = []
        # for c in s:
        #     if c == 'b':
        #         dp += c,
        #     else:
        #         if not dp:
        #             dp += c,
        #         else:
        #             if dp[-1] == 'a':
        #                 dp += c,
        #             else:
        #                 idx = bisect_right(dp, c)
        #                 dp[idx] = c
        # return len(s) - len(dp)
