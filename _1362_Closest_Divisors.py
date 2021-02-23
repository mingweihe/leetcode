class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def find(x):
            ans1, ans2 = 1, x
            for i in xrange(2, int(x**.5)+1):
                if x % i != 0: continue
                ans1, ans2 = i, x / i
            return ans1, ans2
        a, b = find(num+1)
        c, d = find(num+2)
        if abs(a-b) < abs(c-d): return [a, b]
        return [c, d]
