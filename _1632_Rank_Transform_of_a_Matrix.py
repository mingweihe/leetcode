from collections import defaultdict


class Solution(object):
    def matrixRankTransform(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        dic = defaultdict(list)
        for i in xrange(m):
            for j in xrange(n):
                dic[matrix[i][j]] += (i, j),
        ranks = [0] * (m + n)
        
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        for v in sorted(dic):
            p = range(m + n)
            group_ranks = defaultdict(int)
            for i, j in dic[v]:
                i, j = find(i), find(m+j)
                p[i] = j
                group_ranks[j] = max(group_ranks[i], group_ranks[j], ranks[i], ranks[j])
                
            for i, j in dic[v]:
                matrix[i][j] = ranks[i] = ranks[m+j] = group_ranks[find(i)] + 1
        return matrix
