class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Approach 4
        return n == 2 ** (int(n).bit_length() - 1)

        # Approach 3
        # n = float(n)
        # while True:
        #     if n == 1: return True
        #     if n * 10 % 10 or n < 1: return False
        #     n /= 2
        # i = 1
        # while i < n + 1:
        #     if i == n: return True
        #     i *= 2
        # return False

        # Approach 2
        # return n > 0 and 2147483648 % n == 0

        # Approach 1
        # n = float(n)
        # if n == 1: return True
        # if n * 10 % 10 or n < 1: return False
        # return self.isPowerOfTwo(n/2)
