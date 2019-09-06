class Solution(object):
    def fractionToDecimal(self, n, d):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
            straightforward implementation puzzle
            step by step
                case 1: zero + -
                case 2: integer part
                case 3: decimal part
            while dictionary is required to implement it
            dictionary is used for storing recurring decimal digits
        """
        if n == 0: return '0'
        res = '-' * ((n > 0) ^ (d > 0))
        n, d = abs(n), abs(d)
        a, b = divmod(n, d)
        res += `a`
        if b == 0: return res
        res += '.'
        dic = {b: len(res)}
        while b:
            b *= 10
            a, b = divmod(b, d)
            res += `a`
            if b in dic:
                res = res[:dic[b]] + '(' + res[dic[b]:] + ')'
                break
            else:
                dic[b] = len(res)
        return res
