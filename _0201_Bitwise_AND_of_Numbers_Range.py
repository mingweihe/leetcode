class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        offset = 0
        while m != n:
            m>>=1
            n>>=1
            offset += 1
        return m << offset
