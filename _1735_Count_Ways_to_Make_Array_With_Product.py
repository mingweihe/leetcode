class Solution(object):    
    def waysToFillArray(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def comb(n, k):
            ans = 1
            for i in xrange(k):
                ans *= (n-i)
            for i in xrange(1, k+1):
                ans /= i
            return ans
        
        def get_prime_counts(x):
            ans = []
            i = 2
            while i * i <= x:
                cnt = 0
                while x % i == 0:
                    x /= i
                    cnt += 1
                if cnt > 0: ans += cnt,
                i += 1
            if x > 1: ans += 1,
            return ans
        
        res = []
        MOD = 10**9 + 7
        for n, k in queries:
            counts = get_prime_counts(k)
            cur = 1
            for cnt in counts:
                cur *= comb(n+cnt-1, cnt)
            cur %= MOD
            res += cur,
        return res
