import collections


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        adjacencies = collections.defaultdict(list)
        in_degrees = collections.defaultdict(int)
        for c, p in prerequisites:
            adjacencies[p] += [c]
            in_degrees[c] += 1
        queue = [i for i in xrange(numCourses) if i not in in_degrees]
        while queue:
            cur = queue.pop(0)
            res.append(cur)
            for c in adjacencies[cur]:
                in_degrees[c] -= 1
                if in_degrees[c] == 0:
                    queue.append(c)
        if len(res) == numCourses:
            return res
        return []
