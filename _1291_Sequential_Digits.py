class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        len_low, len_high = len(str(low)), len(str(high))
        res = []
        for i in xrange(len_low, len_high+1):
            for j in xrange(1, 10-i+1):
                cur = 0
                for k in xrange(j, j+i):
                    cur = cur*10+k
                if low <= cur <= high:
                    res.append(cur)
        res.sort()
        return res
