class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def backtracking(res, cur, start, k, n):
            if k < 0 or n < 0: return
            if n == 0 and k == 0:
                res.append(list(cur))
            for i in xrange(start, 10):
                cur.append(i)
                backtracking(res, cur, i + 1, k - 1, n - i)
                cur.pop()

        res = []
        backtracking(res, [], 1, k, n)
        return res
