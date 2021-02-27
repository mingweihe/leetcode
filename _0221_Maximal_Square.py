class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
            dp puzzle
        """
        ## Approach 2, variant of finding max rectangle from a histogram
        def get_max_rectangle(A):
            ans, stack = 0, [-1]
            A = A + [0]
            for i, x in enumerate(A):
                while x < A[stack[-1]]:
                    idx = stack.pop()
                    h, w = A[idx], i - stack[-1] - 1
                    ans = max(ans, min(h, w)**2)
                stack += i,
            return ans
        
        m, n = len(matrix), len(matrix[0])
        res, heights = 0, [0] * n
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == '0': heights[j] = 0
                else: heights[j] += 1
            res = max(res, get_max_rectangle(heights))
        return res

        ## Approach 1
        # if not matrix or not matrix[0]: return 0
        # m, n = len(matrix), len(matrix[0])
        # dp = [[0]*(n+1) for _ in xrange(m+1)]
        # max_side = 0
        # for i in xrange(1, m+1):
        #     for j in xrange(1, n+1):
        #         if matrix[i-1][j-1] == '1':
        #             dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        #             max_side = max(max_side, dp[i][j])
        # return max_side*max_side
