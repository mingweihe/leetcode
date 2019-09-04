class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        # Approach 2
        return all(x[0] >= y[1] for x, y in zip(sorted(intervals, key=lambda x: x[0])[1:],
                                                sorted(intervals, key=lambda x: x[0])))
        # Approach 1
        # intervals.sort(key=lambda x: x[0])
        # for i in xrange(1, len(intervals)):
        #     if intervals[i][0] < intervals[i - 1][1]:
        #         return False
        # return True
