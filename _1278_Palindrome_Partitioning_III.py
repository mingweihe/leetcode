class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
            memorized dynamic programming
        """

        def num_change(ss):
            l, r = 0, len(ss) - 1
            cnt = 0
            while l < r:
                if ss[l] != ss[r]: cnt += 1
                l, r = l + 1, r - 1
            return cnt

        def dp(right, kk):
            if (right, kk) not in memo:
                if kk == 1:
                    memo[right, kk] = num_change(s[:right + 1])
                else:
                    ans = float('inf')
                    for i in xrange(kk - 2, right):
                        ans = min(ans, dp(i, kk - 1) + num_change(s[i + 1:right + 1]))
                    memo[right, kk] = ans
            return memo[right, kk]

        memo = {}
        return dp(len(s) - 1, k)
