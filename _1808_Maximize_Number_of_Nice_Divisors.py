class Solution(object):
    def maxNiceDivisors(self, n):
        """
        :type primeFactors: int
        :rtype: int
        """
        MOD = 10**9+7
        if n == 1: return 1
        if n % 3 == 0: return pow(3, n/3, MOD)
        if n % 3 == 1: return 4 * pow(3, (n-4)/3, MOD) % MOD
        return 2 * pow(3, (n-2)/3, MOD) % MOD
