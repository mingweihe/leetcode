class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
            classical topological sort puzzle
        """
        in_degrees = {}
        adjacencies = {}
        for x, y in prerequisites:
            in_degrees[x] = in_degrees.get(x, 0) + 1
            adjacencies[y] = adjacencies.get(y, []) + [x]
        queue = [i for i in xrange(numCourses) if i not in in_degrees]
        course_to_learn = numCourses
        while queue:
            cur = queue.pop(0)
            course_to_learn -= 1
            for c in adjacencies.get(cur, []):
                in_degrees[c] -= 1
                if in_degrees[c] == 0:
                    queue.append(c)
        return course_to_learn == 0
