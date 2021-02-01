class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        last = 2 * (n - 1) + 1
        avg = (last + 1) / 2
        res = 0
        for i in xrange(n/2):
            res += avg - (i*2 + 1)
        return res
