class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l <= r:
            mid = (l + r)//2
            if mid * mid > x:
                r = mid
                r -= 1
            else:
                l = mid
                l += 1
        return r
