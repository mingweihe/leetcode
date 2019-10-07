class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach 2 dynamic programming
        res, n = 0, len(s)
        dp = [[False] * n for _ in xrange(n)]
        for i in xrange(n - 1, -1, -1):
            for j in xrange(i, n):
                if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
                    res += 1
                    dp[i][j] = True
        return res

        # Approach 1 expanding string
        # def expanding(left, right):
        #     ans = 0
        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         ans += 1
        #         left -= 1
        #         right += 1
        #     return ans
        # res = 0
        # for i in xrange(len(s)):
        #     res += expanding(i, i)
        #     res += expanding(i, i+1)
        # return res
