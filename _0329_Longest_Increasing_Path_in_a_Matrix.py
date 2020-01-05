class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(x, y):
            if (x, y) in dic: return dic[x, y]
            ans = 1
            for x1, y1 in dirs:
                x2, y2 = x + x1, y + y1
                if 0 <= x2 < len(matrix) and 0 <= y2 < len(matrix[0]) and matrix[x2][y2] > matrix[x][y]:
                    ans = max(ans, dfs(x2, y2) + 1)
            dic[x, y] = ans
            return ans

        dic = {}
        res = 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                res = max(res, dfs(i, j))
        return res