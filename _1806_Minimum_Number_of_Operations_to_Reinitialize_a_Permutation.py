class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, j = n - 1, n - 2
        i0, j0 = i, j
        cnt = 0
        while True:
            if i % 2 == 0: i /= 2
            else: i = n / 2 + (i - 1) / 2
            if j % 2 == 0: j  /= 2
            else: j = n / 2 + (j - 1) / 2
            cnt += 1
            if i == i0 and j == j0: return cnt
        return -1
