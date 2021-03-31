from collections import defaultdict


class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        ## Approach 2, union find, count by group of couples
        def find(x):
            if roots[x] != x:
                roots[x] = find(roots[x])
            return roots[x]
        n = len(row)
        roots = [0] * n
        for i in xrange(0, n, 2):
            roots[i] = i
            roots[i+1] = i
        for i in xrange(0, n, 2):
            a, b = find(row[i]), find(row[i+1])
            if a != b: roots[a] = b
        cnts = defaultdict(int)
        for i in xrange(n):
            cnts[find(i)] += 1
        ans = 0
        for x in cnts.values():
            ans += x / 2 - 1
        return ans
        
        ## Approach 1, greedy, O(n)
        # d = {x: i for i, x in enumerate(row)}
        # ans = 0
        # for i in xrange(0, len(row), 2):
        #     x = row[i]
        #     nx = row[i+1]
        #     if x % 2 == 0:
        #         cp = x+1
        #         cp_loc = d[cp]
        #     else:
        #         cp = x-1
        #         cp_loc = d[cp]
        #     if cp_loc == i+1: continue
        #     d[cp], d[nx] = d[nx], d[cp]
        #     row[i+1], row[cp_loc] = row[cp_loc], row[i+1]
        #     ans += 1
        # return ans
