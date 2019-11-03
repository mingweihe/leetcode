class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        X, Y = 0, 0
        for i in xrange(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x': X += 1
                else: Y += 1
        if (X+Y) & 1: return -1
        return int(round(X / 2.) + round(Y / 2.))
