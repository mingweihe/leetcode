
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b


def knows(a, b):
    return True


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
            The purpose of this puzzle is to find an algorithm
            to make calls of APIs are as less as possible,
                because calling api costs time in realistic
            so, we employ the idea of exclusion 
        """
        if n < 2: return -1
        candidate = 0
        for i in xrange(1, n):
            if knows(candidate, i):
                candidate = i
        for i in xrange(candidate):
            if knows(candidate, i): return -1
        for i in xrange(n):
            if candidate != i and not knows(i, candidate):
                return -1
        return candidate
