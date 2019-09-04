import math


class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        math O(1)
        1+2+3+...+k=target+d
        """
        target = abs(target)
        k = int(math.ceil(.5*(-1+(1+8*target)**.5)))
        summ = k*(k+1)/2
        d = summ - target
        if d%2 == 0: return k
        return k+1+k%2
