class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in xrange(n):
            res += (i / 7) + (i % 7) + 1
        return res
