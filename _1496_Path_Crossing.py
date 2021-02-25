class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        i, j = 0, 0
        his = set([(0, 0)])
        dirs = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        for k in path:
            i, j = i + dirs[k][0], j + dirs[k][1]
            if (i, j) in his: return True
            his.add((i, j))
        return False
