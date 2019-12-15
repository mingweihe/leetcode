class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        res = 0
        m, n = len(mat), len(mat[0])
        matn = [[0] * (n + 1) for _ in xrange(m + 1)]

        def valid(side, i, j):
            summ = matn[i][j] - matn[i - side][j] - matn[i][j - side] + matn[i - side][j - side]
            if summ > threshold: return False
            return True

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                matn[i][j] = mat[i - 1][j - 1] + matn[i - 1][j] + matn[i][j - 1] - matn[i - 1][j - 1]
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                low, high = 0, min(i, j)
                while low <= high:
                    mid = (low + high) / 2
                    if valid(mid, i, j):
                        low = mid + 1
                    else:
                        high = mid - 1
                res = max(res, high)
        return res
