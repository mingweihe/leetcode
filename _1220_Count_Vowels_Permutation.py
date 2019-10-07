class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int

        """
        M = 10 ** 9 + 7
        a = e = i = o = u = 1
        for _ in xrange(n - 1):
            a1 = (e + i + u) % M
            e1 = (a + i) % M
            i1 = (e + o) % M
            o1 = i % M
            u1 = (i + o) % M
            a, e, i, o, u = a1, e1, i1, o1, u1
        return (a + e + i + o + u) % M
