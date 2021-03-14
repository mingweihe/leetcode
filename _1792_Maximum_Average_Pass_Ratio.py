from heapq import heappush, heappop


class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        def convert(p, t):
            return float(p+1) / (t+1) - float(p) / t
        
        hq = []
        for p, t in classes:
            heappush(hq, [-convert(p, t), p, t])
        while hq and extraStudents:
            _, p, t = heappop(hq)
            p += 1
            t += 1
            heappush(hq, [-convert(p, t), p, t])
            extraStudents -= 1
        total = 0
        for _, p, t in hq:
            total += float(p) / t
        return total / len(hq)
