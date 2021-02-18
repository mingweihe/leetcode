class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        m, n = len(rowSum), len(colSum)
        A = [[0] * n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                A[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= A[i][j]
                colSum[j] -= A[i][j]
        return A
