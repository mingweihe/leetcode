class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            n -= 1
            r = n % 26
            res = chr(r+65) + res
            n //= 26
        return res
