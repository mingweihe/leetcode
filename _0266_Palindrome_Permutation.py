import collections


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return sum(x & 1 for x in collections.Counter(s).values()) < 2
