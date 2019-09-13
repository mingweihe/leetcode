class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
            naive approach time O(n^n))
            optimized approach time O(sqrt(n)^n)
        """
        # Approach 3 time O(sqrt(n)^n), conciser
        def helper(res, cur, i, x):
            while i*i <= x:
                if x % i == 0:
                    res += cur+[i, x/i],
                    helper(res, cur+[i], i, x / i)
                i += 1
            return res
        return helper([], [], 2, n)

        # Approach 2 time O(sqrt(n)^n)
        # def helper(res, cur, x, start):
        #     if x == 1:
        #         if len(cur) > 1:
        #             res.append(list(cur))
        #         return
        #     for i in xrange(start, int(x**.5)+1):
        #         if x % i == 0:
        #             cur.append(i)
        #             helper(res, cur, x / i, i)
        #             cur.append(x / i)
        #             res.append(list(cur))
        #             cur.pop()
        #             cur.pop()
        # res = []
        # helper(res, [], n, 2)
        # return res

        # Approach 1 time O(n^n)
        # def helper(res, cur, x, start):
        #     if x == 1:
        #         if len(cur) > 1:
        #             res.append(list(cur))
        #         return
        #     for i in xrange(start, x+1):
        #         if x % i == 0:
        #             cur.append(i)
        #             helper(res, cur, x / i, i)
        #             cur.pop()
        # res = []
        # helper(res, [], n, 2)
        # return res
