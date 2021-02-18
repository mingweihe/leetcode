from heapq import heappush, heappop
from sortedcontainers import SortedList

class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        num_used = [0] * k
        idle = SortedList([_ for _ in xrange(k)])
        hq = []
        for i, x in enumerate(arrival):
            while hq and x >= hq[0][0]:
                idle.add(hq[0][1])
                heappop(hq)
            if len(hq) == k: continue
            
            idx = idle.bisect_left(i % k)
            
            if idx == len(idle): target_i = idle[0]
            else: target_i = idle[idx]
            idle.discard(target_i)
            heappush(hq, [x+load[i], target_i])
            num_used[target_i] += 1
        maxi = max(num_used)
        return [i for i, x in enumerate(num_used) if x == maxi]
