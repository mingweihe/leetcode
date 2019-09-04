class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n in (1, 2): return 1
        a, b, c = 0, 1, 1
        for i in range(3, n + 1):
            t = c
            c += a + b
            a = b
            b = t
        return c
