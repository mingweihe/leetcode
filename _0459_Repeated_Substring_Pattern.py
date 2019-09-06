class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Approach 3
        return s in (s+s)[1:-1]

        # Approach 2
        # j = len(s)//2+1
        # for i in range(1, len(s)//2+1):
        #     if s.count(s[:i])*i==len(s): return True
        # return False

        # Approach 1
        # i, j, n = 1, 0, len(s)
        # dp = [0] * (n + 1)
        # while i < n:
        #     if s[i] == s[j]:
        #         i += 1
        #         j += 1
        #         dp[i] = j
        #     elif j == 0:
        #         i += 1
        #     else:
        #         j = dp[j]
        # return bool(dp[n] and dp[n] % (n - dp[n]) == 0)
