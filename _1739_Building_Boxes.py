class Solution(object):
    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur = side = extra = 0
        while cur + (side+1) * (side+2) / 2 <= n:
            cur += (side+1) * (side+2) / 2
            side += 1
        while cur < n:
            extra += 1
            cur += extra
        return side * (side+1) / 2 + extra
