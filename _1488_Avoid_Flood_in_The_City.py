from collections import defaultdict, deque
from heapq import heappop, heappush


class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        urgent = []
        lake_days = defaultdict(deque)
        for i, lake in enumerate(rains):
            lake_days[lake].append(i)
        res = []
        for i, lake in enumerate(rains):
            if urgent and urgent[0] == i:
                return []
            if not lake:
                if not urgent:
                    res.append(1)
                    continue
                day = heappop(urgent)
                res.append(rains[day])
            else:
                days = lake_days[lake]
                days.popleft()
                if days:
                    heappush(urgent, days[0])
                res.append(-1)
        return res
