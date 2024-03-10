class Solution(object):
    def maximumHappinessSum(self, h, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        dec, n = 0, len(h)
        h.sort()
        res = 0
        for i in xrange(n-1, -1, -1):
            if k == 0: break
            k -= 1
            res += max(0, h[i] - dec)
            dec += 1
        return res
