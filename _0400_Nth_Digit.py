class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = 9, 1
        while i < n:
            j += 1
            i += 9 * j * 10 ** (j - 1)
        i -= 9 * j * 10 ** (j - 1)
        index = n - i - 1
        return int(str(10 ** (j - 1) + index // j)[index % j])
