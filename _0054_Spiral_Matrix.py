import numpy as np


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Approach 2 iteration
        top, bottom, left = 0, len(matrix) - 1, 0
        right = -1 if not matrix else len(matrix[0]) - 1
        l = (bottom + 1) * (right + 1)
        res = [0] * l
        i = 0
        while i < l:
            j = left
            while j <= right:
                res[i] = matrix[top][j]
                i, j = i + 1, j + 1
            j = top = top + 1
            if i == l: break
            while j <= bottom:
                res[i] = matrix[j][right]
                i, j = i + 1, j + 1
            j = right = right - 1
            if i == l: break
            while j >= left:
                res[i] = matrix[bottom][j]
                i, j = i + 1, j - 1
            j = bottom = bottom - 1
            if i == l: break
            while j >= top:
                res[i] = matrix[j][left]
                i, j = i + 1, j - 1
            left += 1
            if i == l: break
        return res

        # Approach 1 numpy and recursion
        # return [] if not matrix else list(matrix[0]) + self.spiralOrder(np.transpose(matrix[1:])[::-1].tolist())
