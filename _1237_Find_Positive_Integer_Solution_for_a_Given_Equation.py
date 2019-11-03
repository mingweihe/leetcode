"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""


class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        # Approach 3 time O(n)
        res = []
        j = 1000
        for i in xrange(1, 1001):
            while j > 1 and customfunction.f(i, j) > z: j -= 1
            if customfunction.f(i, j) == z:
                res.append([i, j])
        return res
        # Approach 1 time O(n^2)
        # res = []
        # for i in xrange(1, 1001):
        #     j = 1
        #     cur = customfunction.f(i, j)
        #     if cur > z: break
        #     while cur <= z:
        #         if cur == z:
        #             res.append([i, j])
        #         j += 1
        #         cur = customfunction.f(i, j)
        # return res
