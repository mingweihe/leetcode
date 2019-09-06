import string
import operator
from functools import reduce


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Approach 4
        return chr(reduce(operator.xor, map(ord, s + t)))

        # Approach 3
        # return chr(reduce(lambda x, y: x ^ y, map(ord, s + t)))

        # Approach 2
        # return chr(sum(map(ord, t)) - sum(map(ord, s)))

        # Approach 1
        # return [i for i in string.ascii_lowercase if s.count(i) != t.count(i)][0]
