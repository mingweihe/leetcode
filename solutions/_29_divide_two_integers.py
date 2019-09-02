class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0: return 0
        sign = 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            sign = -1
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor: return 0
        res = self.helper(dividend, divisor)
        if sign == 1 and res > 2147483647: return 2147483647
        if sign == -1:
            if res > 2147483648: return -2147483648
            return -res
        return res

    def helper(self, dividend, divisor):
        if dividend < divisor: return 0
        summ, multiple = divisor, 1
        while summ + summ <= dividend:
            summ += summ
            multiple += multiple
        return multiple + self.helper(dividend - summ, divisor)

