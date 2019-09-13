class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """

        def helper(n, m):
            if n == 0: return ['']
            if n == 1: return ['0', '1', '8']
            res = []
            ls = helper(n - 2, m)
            for x in ls:
                if n != m: res.append('0' + x + '0')
                res.append('1' + x + '1')
                res.append('6' + x + '9')
                res.append('8' + x + '8')
                res.append('9' + x + '6')
            return res

        res = 0
        for i in xrange(len(low), len(high) + 1):
            ls = helper(i, i)
            for x in ls:
                if len(x) == len(low) and x < low: continue
                if len(x) == len(high) and x > high: continue
                res += 1
        return res
