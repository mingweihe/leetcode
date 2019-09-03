class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return 0
        res, isPrime = 0, [1]*n
        isPrime[0] = isPrime[1] = 0
        for i in range(2, int(n**.5) + 1):
            if isPrime[i]: isPrime[i*i:n:i] = [0]*len(isPrime[i*i:n:i])
        return sum(isPrime)
