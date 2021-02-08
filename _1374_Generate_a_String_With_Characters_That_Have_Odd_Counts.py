class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        return 'a' * n if n & 1 else (n-1) * 'a' + 'b'
