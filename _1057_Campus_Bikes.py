import heapq


class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        # Approach 2 Bucket Sort Algorithm, time O(m*n)
        dists = [[] for _ in xrange(2001)]
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                d = abs(w[0] - b[0]) + abs(w[1] - b[1])
                dists[d].append([i, j])
        res = [-1] * len(workers)
        assigned_bikes = set()
        for x in dists:
            for i, j in x:
                if res[i] == -1 and j not in assigned_bikes:
                    res[i] = j
                    assigned_bikes.add(j)
        return res

        # Approach 1 Priority Queue, time O(m*n*log(m))
        # hq, w2b = [], collections.defaultdict(list)
        # for i, (wx, wy) in enumerate(workers):
        #     for j, (bx, by) in enumerate(bikes):
        #         dis = abs(wx-bx) + abs(wy-by)
        #         w2b[i].append([dis, i, j])
        #     w2b[i].sort(reverse=True)
        #     heapq.heappush(hq, w2b[i].pop())
        # res = [0]*len(workers)
        # assigned_bikes = set()
        # while len(assigned_bikes) < len(workers):
        #     _, i, j = heapq.heappop(hq)
        #     if j not in assigned_bikes:
        #         assigned_bikes.add(j)
        #         res[i] = j
        #     else:
        #         heapq.heappush(hq, w2b[i].pop())
        # return res
