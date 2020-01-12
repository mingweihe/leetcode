class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        roots = list(xrange(n))

        def find(nn):
            if roots[nn] != nn:
                roots[nn] = find(roots[nn])
            return roots[nn]

        num_spared_lines = 0
        for a, b in connections:
            _a, _b = find(a), find(b)
            if _a != _b:
                roots[_a] = _b
            else:
                num_spared_lines += 1
        for x in xrange(n): find(x)
        num_lines_needed = len(set(roots)) - 1
        if num_spared_lines >= num_lines_needed:
            return num_lines_needed
        return -1
