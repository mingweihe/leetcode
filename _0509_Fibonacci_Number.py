class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        a,b=0,1
        for i in range(1, N+1):
            a,b = b,a+b
        return a
