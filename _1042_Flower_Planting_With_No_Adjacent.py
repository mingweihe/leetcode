import collections


class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        res = [0] * N
        for x, y in paths:
            graph[x].add(y)
            graph[y].add(x)
        for i in xrange(1, N+1):
            res[i-1] = ({1,2,3,4} - {res[j-1] for j in graph[i]}).pop()
        return res
