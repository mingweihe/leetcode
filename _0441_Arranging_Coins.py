import math


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach 3
        return int((math.sqrt(1 + 8 * n) - 1) / 2)

        # Approach 2
        # i, c = 0, 0
        # while c < n:
        #     i += 1
        #     c += i
        # if c > n: return i - 1
        # return i

        # Approach 1
        # l, r = 0, n
        # while l <= r:
        #     m = l + (r-l)//2
        #     if (m+1)*m//2 <= n: l = m + 1
        #     else: r = m - 1
        # return r
