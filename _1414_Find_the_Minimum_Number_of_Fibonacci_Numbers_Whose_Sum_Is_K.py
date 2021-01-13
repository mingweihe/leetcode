class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        ## Approach 2
        res, a, b = 0, 1, 1
        while b <= k:
            a, b = b, a + b
        while k:
            if a <= k:
                k -= a
                res += 1
            a, b = b - a, a
        return res
        
        ## Approach 1
        # @lru_cache(None)
        # def fib(x):
        #     if x == 1 or x == 2: return 1
        #     return fib(x-1) + fib(x-2)
        # hq = []
        # i = 1
        # cur = 1
        # while cur <= k:
        #     cur = fib(i)
        #     heappush(hq, -cur)
        #     i += 1
        # res = 0
        # while k:
        #     cur = -heappop(hq)
        #     while k-cur >= 0:
        #         k -= cur
        #         res += 1
        # return res
