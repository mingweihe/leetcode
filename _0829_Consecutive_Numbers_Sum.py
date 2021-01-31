class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        N = 1+2+3+...+n + n + n
        """
        n, ans = 2, 1
        summ = n * (n+1) / 2
        while summ <= N:
            if (N - summ) % n == 0:
                ans += 1
            n += 1
            summ = n * (n+1) / 2
        return ans
