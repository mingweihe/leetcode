class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str: return 0
        res, sign, start = 0, 1, 0
        if str[0] == '-':
            sign = -1
            start += 1
        elif str[0] == '+':
            start += 1
        for i in xrange(start, len(str)):
            if not str[i].isdigit():
                return sign * res
            res = res * 10 + int(str[i])
            if sign == 1 and res > 2147483647:
                return 2147483647
            if sign == -1 and res > 2147483648:
                return -2147483648
        return sign * res
