class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ## simplified
        res = []
        k-=n
        while n > 0:
            tmp = min(25, k)
            res += chr(97+tmp),
            k-=tmp
            n-=1
        return ''.join(res[::-1])
            
        ## Original version
        # res = []
        # for i in xrange(26, 0, -1):
        #     while k-i >= n-1:
        #         res += chr(96+i),
        #         k-=i
        #         n-=1
        #         if n == 0:
        #             return ''.join(res)[::-1]
