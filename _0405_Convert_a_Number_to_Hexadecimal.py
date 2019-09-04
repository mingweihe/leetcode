import string


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        res = ''
        if num < 0: num += 2**32
        while num:
            res = string.hexdigits[num%16] + res
            num >>= 4
        return res
