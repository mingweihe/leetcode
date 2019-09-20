class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
            disjoint / union find sets
        """
        dirs = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        roots = [-1] * (m * n)
        res, count = [], 0
        for p in positions:
            root = p[0] * n + p[1]
            if roots[root] != -1:
                res.append(res[-1])
                continue
            roots[root] = root
            count += 1
            for dr in dirs:
                i, j = p[0] + dr[0], p[1] + dr[1]
                np = i * n + j
                if i < 0 or i == m or j < 0 or j == n or roots[np] == -1: continue
                new_root = self.find(roots, np)
                if new_root != root:
                    roots[root] = new_root
                    root = new_root
                    count -= 1
            res.append(count)
        return res

    def find(self, roots, idx):
        while idx != roots[idx]:
            idx = roots[idx]
        return idx
