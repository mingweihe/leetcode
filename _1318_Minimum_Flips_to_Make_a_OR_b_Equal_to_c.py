class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        # Approach 2
        res, mark = 0, 1
        while mark <= a or mark <= b or mark <= c:
            if mark & c:
                res += int(mark & a == mark & b == 0)
            else:
                res += int(mark & a != 0) + int(mark & b != 0)
            mark <<= 1
        return res

        # Approach 1
        # res = 0
        # a, b, c = bin(a)[2:].zfill(32), bin(b)[2:].zfill(32), bin(c)[2:].zfill(32)
        # for i in xrange(32):
        #     if c[i] == '1':
        #         res += int(a[i] == b[i] == '0')
        #     else:
        #         res += int(a[i]) + int(b[i])
        # return res
