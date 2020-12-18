from bisect import bisect_left, insort


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        m, n = len(matrix), len(matrix[0])
        for i in xrange(1, m):
            for j in xrange(n):
                matrix[i][j] += matrix[i-1][j]

        def maxSumSubArray(arr):
            sub_max = float('-inf')
            pre_sum = [float('inf')]
            cur_sum = 0
            for x in arr:
                insort(pre_sum, cur_sum) 
                cur_sum += x
                i = bisect_left(pre_sum, cur_sum-k)
                sub_max = max(sub_max, cur_sum - pre_sum[i])         
            return sub_max
        
        res = float('-inf')
        for i in xrange(m):
            for j in xrange(i, m):
                A = [matrix[j][p] - (matrix[i-1][p] if i > 0 else 0) for p in xrange(n)]
                res = max(res, maxSumSubArray(A))
        return res
