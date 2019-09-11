class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        calculate 1s at each location/digit
            eg: calculating 1s at hundred digit
            case 1: 0
                eg: 12093
                res += 12*100, 12 is 12093 / 100 / 10
            case 2: 1
                eg: 12193
                res += 12*100+(93+1)
            case 3: >=2
                eg: 12593
                res += (12+1)*100
        """
        m = 1
        res = 0
        while m <= n:
            a, b = divmod(n, m)
            res += (a+8) / 10 * m
            if a % 10 == 1: res += b+1
            m *= 10
        return res
