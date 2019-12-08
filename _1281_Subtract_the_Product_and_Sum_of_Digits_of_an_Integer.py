class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s, p = 0, 1
        while n:
            cur = n % 10
            s += cur
            p *= cur
            n /= 10
        return p - s
