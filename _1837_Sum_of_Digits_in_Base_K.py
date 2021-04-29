class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ans = 0
        while n:
            n, r = divmod(n, k)
            ans += r
        return ans
