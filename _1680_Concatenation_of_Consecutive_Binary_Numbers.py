class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## Approach 2
        MOD = 10**9+7
        shift = 2
        res = 0
        for i in xrange(1, n+1):
            if i == shift: shift<<=1
            res = res * shift + i
            res %= MOD
        return res
        
        ## Approach 1, python bin, int
        # res = ''
        # MOD = 10**9+7
        # for i in xrange(1, n+1):
        #     res += bin(i)[2:]
        # return int(res, 2) % MOD
