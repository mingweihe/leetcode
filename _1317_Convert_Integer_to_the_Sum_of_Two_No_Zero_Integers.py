class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for a in xrange(1, n):
            b = n - a
            if '0' not in str(a) and '0' not in str(b):
                return [a, b]
