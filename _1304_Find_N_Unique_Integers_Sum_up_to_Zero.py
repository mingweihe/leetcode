class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Approach 2
        return list(xrange(n - 1)) + [-(n - 1) * (n - 2) / 2]
        # Approach 1
        # res = []
        # if n & 1:
        #     res += 0,
        #     n -= 1
        # cur = 1
        # while n:
        #     res += cur,
        #     res += -cur,
        #     cur += 1
        #     n -= 2
        # return res
