class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach 2
        if n==1: return 9
        if n==2: return 987
        for a in xrange(2, 9*10**(n-1)):
            hi=(10**n)-a
            lo=int(str(hi)[::-1])
            if a**2-4*lo < 0: continue
            if (a**2-4*lo)**.5 == int((a**2-4*lo)**.5):
                return (lo+10**n*(10**n-a))%1337

        # Approach 1
        # if n == 1: return 9
        # upperBound=10**n-1
        # lowerBound=upperBound//10+1
        # maxValue = upperBound**2
        # half = maxValue//(upperBound+1)
        # while True:
        #     _h = str(half)
        #     pStr = _h+_h[::-1]
        #     pInt = int(pStr)
        #     i = upperBound
        #     while i > lowerBound-1:
        #         if i*i<pInt: break
        #         if pInt%i == 0: return pInt%1337
        #         i-=1
        #     half-=1
