class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Approach 2 time O(m+n)
        if not matrix or not matrix[0]: return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

        # Approach 1 time O(n^log4(3))
        # if not matrix or not matrix[0]: return False
        # def helper(x1, y1, x2, y2):
        #     if x1 > x2 or y1 > y2: return False
        #     x, y = (x1+x2) / 2, (y1+y2) / 2
        #     if matrix[x][y] == target: return True
        #     elif matrix[x][y] > target:
        #         return helper(x1, y1, x-1, y-1) \
        #             or helper(x, y1, x2, y-1) \
        #             or helper(x1, y, x-1, y2)
        #     else:
        #         return helper(x+1, y+1, x2, y2) \
        #             or helper(x+1, y1, x2, y) \
        #             or helper(x1, y+1, x, y2)
        # return helper(0, 0, len(matrix)-1, len(matrix[0])-1)
