from heapq import heappush, heappop


class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        tasks = sorted([(e, p, i) for i, (e, p) in enumerate(tasks)])
        ans, ct = [], tasks[0][0]
        i = 0
        hq = []
        while hq or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= ct:
                heappush(hq, [tasks[i][1], tasks[i][2]])
                i += 1
            if not hq:
                ct = tasks[i][0]
                continue
            p, idx = heappop(hq)
            ans += idx,
            ct += p
        return ans
