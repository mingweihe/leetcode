import heapq


class Solution(object):
    def maxEvents(self, e):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        heapq.heapify(e)
        res, last_available = 0, 0
        while e:
            while e[0][0] == last_available and e[0][0] < e[0][1]:
                heapq.heapreplace(e, [e[0][0]+1, e[0][1]])
            last_available = max(heapq.heappop(e)[0], last_available+1)
            res += 1
            while e and last_available >= e[0][1]: heapq.heappop(e)
        return res
