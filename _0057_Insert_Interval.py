class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        i, L, res = 0, len(intervals), []
        while i < L and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < L and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        while i < L:
            res.append(intervals[i])
            i += 1
        return res
