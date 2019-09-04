class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Approach 1
        return n % 4 > 0
        # Approach 2
        # return n ^ (n >> 2 << 2) > 0

