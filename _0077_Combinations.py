from itertools import combinations


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        backtracking
        """
        # Approach 2
        return list(combinations(xrange(1, n+1), k))

        # Approach 1
    #     res = []
    #     self.helper(res, [], n, k, 1)
    #     return res
    #
    # def helper(self, res, cur, n, k, start):
    #     if k == 0:
    #         res.append(list(cur))
    #         return
    #
    #     for i in xrange(start, n - k + 2):  # it's better to write a range bound
    #         cur.append(i)
    #         self.helper(res, cur, n, k - 1, i + 1)  # here is i+1, it's not start+1
    #         cur.pop()
