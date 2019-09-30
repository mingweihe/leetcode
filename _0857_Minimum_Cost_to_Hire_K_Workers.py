import heapq


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
            idea: for eavery ratio, find the minimum total wage for K workers
            data structure: heap
        """
        res, hq, sum_quality = float('inf'), [], 0
        workers = sorted([float(w) / q, q] for q, w in zip(quality, wage))
        for r, q in workers:
            sum_quality += q
            heapq.heappush(hq, -q)
            if len(hq) > K: sum_quality += heapq.heappop(hq)
            if len(hq) == K: res = min(res, sum_quality * r)
        return res
