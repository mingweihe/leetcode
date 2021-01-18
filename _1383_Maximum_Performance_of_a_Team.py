from heapq import heappush, heappop


class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        A = sorted(zip(efficiency, speed), reverse=True)
        hq = []
        res, summ = 0, 0
        for e, s in A:
            summ += s
            heappush(hq, s)
            if len(hq) > k:
                summ -= heappop(hq)
            res = max(res, summ * e)
        return res % MOD
