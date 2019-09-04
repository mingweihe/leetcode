class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
            10e9 is not 10^9
            1e9 is 10^9
            anyway, we can also write as pow(10, 9)
        """
        def factorial(x):
            r = 1
            while x:
                r *= x
                r %= 1000000007
                x -= 1
            return r
        num_prime = 0
        for i in xrange(2, n + 1):
            is_prime = True
            for j in xrange(2, int(i ** .5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                num_prime += 1
        a = factorial(num_prime)
        b = factorial(n - num_prime)
        return a * b % 1000000007
