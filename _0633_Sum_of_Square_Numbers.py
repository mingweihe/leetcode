class Solution(object):

    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # Approach 1
        i = 2
        while i * i <= c:
            cnt = 0
            while c % i == 0:
                cnt += 1
                c /= i
            if i % 4 == 3 and cnt & 1: return False
            i += 1
        return c % 4 != 3
        # Approach 2
        # def is_squared(N):
        #     return N == int(N**.5)**2
        # return any(is_squared(c-x**2) for x in range(int(c**.5)+1))
