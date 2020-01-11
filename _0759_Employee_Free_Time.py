import heapq


# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end


class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        schedule = [interval for x in schedule for interval in x]
        schedule.sort(key=lambda x: x.start)
        hq = [-schedule[0].end]
        res = []
        for i in xrange(1, len(schedule)):
            print type(schedule[i])
            cur_start = schedule[i].start
            cur_end = schedule[i].end
            if cur_start > -hq[0]: res += Interval(-hq[0], cur_start),
            if cur_end > -hq[0]: heapq.heapreplace(hq, -cur_end)
        return res
