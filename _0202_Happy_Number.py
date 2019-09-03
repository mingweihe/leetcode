class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 9:
            t = n
            n = 0
            while t:
                n += pow(t % 10, 2)
                t //= 10
        return n == 1 or n == 7
