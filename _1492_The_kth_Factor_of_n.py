class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # Approach 2, O(sqrt(n))
        a, b = [], []
        for i in xrange(1, int(n**.5)+1):
            if n % i == 0:
                a += i,
                b += n / i,
        if a[-1] == b[-1]: b.pop()
        a += b[::-1]
        return -1 if len(a) < k else a[k-1]
    
        # Approach 1, O(n)
        # cnt = 0
        # for i in xrange(1, n + 1):
        #     if n % i == 0:
        #         cnt += 1
        #         if cnt == k: return i
        # return -1
