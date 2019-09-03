class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        1 << n is faster than 2**n, same idea x >> 1 is better than n / 2
        000 0
        001 1
        011 3
        010 2
        110 6
        111 7
        101 5
        100 4
        G(i) = i ^ (i/2)
        """
        # Approach 2 : iteration
        res = [0]
        for i in xrange(n):
            for j in xrange(len(res) - 1, -1, -1):
                res.append(res[j] | 1 << i)
        return res
        # Approach 1 : formula G(i) = i ^ (i/2)
        # res = []
        # for i in xrange(1 << n):
        #     res.append(i ^ i >> 1)
        # return res
