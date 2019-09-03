class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        pool = list(xrange(1, n+1))
        fact = [1]*n
        for i in xrange(1, n):
            fact[i] = i * fact[i-1]
        k -= 1
        res = ''
        for i in xrange(n-1, -1, -1):
            index = k / fact[i]
            k = k % fact[i]
            res += str(pool[index])
            pool.pop(index)
        return res
