class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = arr[0]
        s0, s1 = arr[0], 0
        for i in xrange(1, len(arr)):
            s1 = max(arr[i]+s1, arr[i], s0)
            s0 = max(arr[i]+s0, arr[i])
            res = max(res, s1)
        return res
