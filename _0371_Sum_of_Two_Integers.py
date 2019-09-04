class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0: return b
        if b == 0: return a
        MAX, mask = 0x7fffffff, 0xFFFFFFFF
        while b: a, b = (a ^ b) & mask, (a & b) << 1 & mask
        return a if a <= MAX else ~(a ^ mask)
