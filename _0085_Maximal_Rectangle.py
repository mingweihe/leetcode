class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        follow up of problem 84
        """
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0]*(n+1)
        res = 0
        for i in xrange(m):
            stack = []
            for j in xrange(n+1):
                if j < n:
                    if matrix[i][j] == '0': heights[j] = 0
                    else: heights[j] += 1
                while stack and heights[j] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = j-(-1 if not stack else stack[-1])-1
                    res = max(res, height*width)
                stack.append(j)
        return res
