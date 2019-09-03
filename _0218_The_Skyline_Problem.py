import heapq


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # Approach 2 O(n*log(n))
        res = [[0, 0]]
        hq = [[0, float('inf')]]
        event = [[l, -h, r] for l, r, h in buildings]
        event += [[r, 0, 0] for _, r, _ in buildings]
        event.sort()
        for l, h, r in event:
            if h != 0: heapq.heappush(hq, [h, r])
            while l >= hq[0][1]: heapq.heappop(hq)
            if res[-1][1] != -hq[0][0]:
                res.append([l, -hq[0][0]])
        return res[1:]
        # Approach 1 O(n^2) -> TLE
        # res, heights = [], []
        # for x in buildings:
        #     heights.append([x[0], -x[2]])
        #     heights.append([x[1], x[2]])
        # heights.sort()
        # hq = [0]
        # prev = 0
        # for x in heights:
        #     if x[1] < 0:
        #         heapq.heappush(hq, x[1])
        #     else:
        #         hq.pop(hq.index(-x[1]))
        #         heapq.heapify(hq)
        #     if hq[0] != prev:
        #         res.append([x[0], -hq[0]])
        #         prev = hq[0]
        # return res
