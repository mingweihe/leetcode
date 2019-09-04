import heapq


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        # Approach 3
        return heapq.nsmallest(K, points, lambda (x, y): x*x+y*y)

        # Approach 2
        # return sorted(points, key=lambda (x, y): x*x+y*y)[:K]

        # Approach 1
        # heap = []
        # for (x, y) in points:
        #     if len(heap) == K:
        #         heapq.heappushpop(heap, [-(x*x+y*y), x, y])
        #     else:
        #         heapq.heappush(heap, [-(x*x+y*y), x, y])
        # return [[x, y] for dist, x,y in heap]
