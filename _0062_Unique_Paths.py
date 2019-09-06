class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Approach 2 math combination computation
        # time O(m) space O(1)
        n = m + n - 2
        k = m - 1
        res = 1
        # return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
        for i in xrange(1, k + 1):
            res *= n - i + 1
        for i in xrange(1, k + 1):
            res /= i
        return res

        # Approach 1 dynamic programming
        # if m == 0 or n == 0: return 0
        # grid = [1]*n
        # for i in xrange(1, m):
        #     for j in xrange(1, n):
        #         grid[j] += grid[j-1]
        # return grid[-1]
