import bisect


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Time O(log(m)*log(n))
        if not matrix or len(matrix[0]) == 0: return False
        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while up <= down:
            mid = (up + down) / 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return matrix[mid][bisect.bisect_left(matrix[mid], target)] == target
            elif matrix[mid][0] > target:
                down = mid - 1
            else:
                up = mid + 1
        return False
