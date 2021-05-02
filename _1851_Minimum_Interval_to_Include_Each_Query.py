class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        hq, d = [], {}
        A = sorted(intervals)[::-1]
        for q in sorted(queries):
            while A and A[-1][0] <= q:
                i, j = A.pop()
                heappush(hq, [j-i+1, j])
            while hq and hq[0][1] < q:
                heappop(hq)
            d[q] = hq[0][0] if hq else -1
        return [d[q] for q in queries]
