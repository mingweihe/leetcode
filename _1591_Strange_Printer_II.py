class Solution(object):
    def isPrintable(self, targetGrid):
        """
        :type targetGrid: List[List[int]]
        :rtype: bool
        """
        m, n = len(targetGrid), len(targetGrid[0])
        colors = set()
        pos = [[m, 0, n, 0] for _ in xrange(61)]
        for i in xrange(m):
            for j in xrange(n):
                color = targetGrid[i][j]
                colors.add(color)
                pos[color][0] = min(pos[color][0], i)
                pos[color][1] = max(pos[color][1], i)
                pos[color][2] = min(pos[color][2], j)
                pos[color][3] = max(pos[color][3], j)
        def test(color):
            for i in xrange(pos[color][0], pos[color][1]+1):
                for j in xrange(pos[color][2], pos[color][3]+1):
                    if targetGrid[i][j] and targetGrid[i][j] != color: return False
            for i in xrange(pos[color][0], pos[color][1]+1):
                for j in xrange(pos[color][2], pos[color][3]+1):
                    targetGrid[i][j] = 0
            return True
        while colors:
            colors2 = set()
            for c in colors:
                if not test(c): colors2.add(c)
            if len(colors) == len(colors2):
                return False
            colors = colors2
        return True
