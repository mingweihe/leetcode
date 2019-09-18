class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
            think as the view of dp algorithm
            current state thought
            case 1: same color with previous one
            case 2: different color with previous one
        """
        if n == 0: return 0
        if n == 1: return k
        same, diff, total = 0, k, k
        for i in xrange(1, n):
            same = diff
            diff = total * (k - 1)
            total = same + diff
        return total
