class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """

        def gcd(x, y):
            # Approach 2
            while y:
                x, y = y, x % y
            return x
            # Approach 1
            # if y == 0: return x
            # return gcd(y, x % y)

        def lcm(x, y):
            return x * y / gcd(x, y)

        def count(x):
            total = x / a + x / b + x / c
            ab, ac, bc = lcm(a, b), lcm(a, c), lcm(b, c)
            total -= x / ab + x / ac + x / bc
            total += x / lcm(ab, c)
            return total

        lo, hi = 1, 2000000000
        while lo <= hi:
            m = (lo + hi) / 2
            if count(m) >= n:
                hi = m - 1
            else:
                lo = m + 1
        return lo
