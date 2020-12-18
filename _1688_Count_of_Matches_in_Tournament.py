class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n != 1:
            if n & 1:
                res += (n - 1) / 2
                n = (n - 1) / 2 + 1
            else:
                res += n/2
                n /= 2
        return res
