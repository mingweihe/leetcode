class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## Approach 2, dp
        if n == 0: return 1
        dp = [9]
        for i in xrange(1, n):
            dp += dp[-1] * (10-i),
        return sum(dp) + 1
            
        ## Approach 1, backtracking
#         def dfs(cur, remain):
#             if remain == 0: return 1
#             ans = 0
#             for nex in xrange(10):
#                 if nex in seen: continue
#                 seen.add(nex)
#                 ans += dfs(nex, remain-1)
#                 seen.discard(nex)
#             return ans
        
#         res = 0
#         for i in xrange(1, n+1):
#             seen = {1}
#             res += dfs(1, i-1) * 9
#         return res + 1
