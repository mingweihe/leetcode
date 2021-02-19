class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        if len(arr) == m: return m
        A = [0] * (len(arr) + 2)
        res = -1
        for i, x in enumerate(arr):
            left, right = A[x-1], A[x+1]
            if left == m or right == m:
                res = i
            A[x-left] = A[x+right] = left + right + 1
        return res
