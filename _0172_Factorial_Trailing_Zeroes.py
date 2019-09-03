class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach 1
        seed, res = 5, 0
        while seed <= n:
            res += n // seed
            seed *= 5
        return res
        # Approach 2
        # return 0 if n < 5 else n // 5 + self.trailingZeroes(n // 5)
