class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        trailing_zeros = []
        n = len(grid)
        for row in grid:
            for i in xrange(n-1, -1, -1):
                if row[i] == 1: break
            trailing_zeros += n-i-1,
        ans = 0
        for i in xrange(n):
            target = n - i - 1
            k = i
            while k < n and trailing_zeros[k] < target:
                k += 1
            if k == n: return -1
            ans += k-i
            while k > i:
                trailing_zeros[k], trailing_zeros[k-1] = trailing_zeros[k-1], trailing_zeros[k]
                k -= 1
        return ans
