class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        Dynamic programming
            - divide by last digit and non last digit
        dp[i] = 0 # invalid
        dp[i] = 1 # valid and same
        dp[i] = 2 # valid and different
        """
        cnt = 0
        dp = [0] * (N + 1)
        for i in range(N + 1):
            if i < 10:
                if i in [0, 1, 8]:
                    dp[i] = 1
                elif i in [2, 5, 6, 9]:
                    dp[i] = 2
                    cnt += 1
            else:
                a, b = i / 10, i % 10
                if dp[a] == 1 and dp[b] == 1:
                    dp[i] = 1
                elif dp[a] >= 1 and dp[b] >= 1:
                    dp[i] = 2
                    cnt += 1
        return cnt
