class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        ans = start
        for i in xrange(1, n):
            ans ^= (start + 2 * i)
        return ans
