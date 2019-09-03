class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        a = sorted(intervals, key=lambda x:x[0])
        res = a[0:1]
        for i in range(1, len(a)):
            if a[i][0] > res[-1][1]: 
                res.append(a[i])
            else: 
                res[-1][1] = max(a[i][1], res[-1][1])
        return res
