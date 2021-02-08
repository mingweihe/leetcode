from collections import defaultdict


class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = defaultdict(int)
        maxi = 0
        for i in xrange(1, n+1):
            summ = 0
            while i:
                i, x = divmod(i, 10)
                summ += x
            d[summ] += 1
            maxi = max(maxi, d[summ])
        return len(filter(lambda x: x == maxi, d.values()))
