import re


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Approach 3
        return re.match('^0b(1*|0)$', bin(n ^ n >> 1))

        # Approach 2
        # return not (n^n>>1)&(n^n>>1)+1

        # Approach 1
        # return re.match('^0b(10)*1?$', bin(n))
