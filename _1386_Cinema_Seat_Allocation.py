from collections import defaultdict


class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        ## Approach 3
        seats = defaultdict(set)
        for i, j in reservedSeats:
            if j in (2, 3, 4, 5):
                seats[i].add(0)
            if j in (4, 5, 6, 7):
                seats[i].add(1)
            if j in (6, 7, 8, 9):
                seats[i].add(2)
        res = n * 2
        for ss in seats.values():
            if len(ss) == 3: res -= 2
            else: res -= 1
        return res
        
        ## Approach 2, from William Lin
        # d = defaultdict(list)
        # for i, j in reservedSeats:
        #     d[i] += j-1,
        # res = (n - len(d)) * 2
        # for cols in d.values():
        #     vals = [0] * 10
        #     for c in cols: vals[c] = 1
        #     ok = 1
        #     for i in xrange(1, 5):
        #         ok &= not vals[i]
        #     if ok:
        #         for i in xrange(1, 5): vals[i] = 1
        #         res += 1
        #     ok = 1
        #     for i in xrange(3, 7):
        #         ok &= not vals[i]
        #     if ok:
        #         for i in xrange(3, 7): vals[i] = 1
        #         res += 1
        #     ok = 1
        #     for i in xrange(5, 9):
        #         ok &= not vals[i]
        #     if ok: res += 1
        # return res
        
        ## Approach 1
        # rows = set()
        # reservedSeats.sort()
        # res = 0
        # m = len(reservedSeats)
        # for i, (r, c) in enumerate(reservedSeats):
        #     rows.add(r)
        #     pc = 0 if i == 0 or reservedSeats[i-1][0] != r else reservedSeats[i-1][1]
        #     nc = 11 if i == m-1 or reservedSeats[i+1][0] != r else reservedSeats[i+1][1]
        #     if pc <= 1 and c >= 10: res += 2
        #     elif pc <= 1 and c >= 6 or pc <= 3 and c >= 8 or pc <= 5 and c >= 10:
        #         res += 1
        #     if nc == 11:
        #         if c <= 1: res += 2
        #         elif c <= 5: res += 1
        # return (n - len(rows)) * 2 + res
