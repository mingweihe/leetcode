class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        res = []
        arr.sort()
        mini = float('inf')
        for i in xrange(1, len(arr)):
            mini = min(mini, arr[i]-arr[i-1])
        for i in xrange(1, len(arr)):
            if arr[i] - arr[i-1] == mini:
                res.append([arr[i-1], arr[i]])
        return res
