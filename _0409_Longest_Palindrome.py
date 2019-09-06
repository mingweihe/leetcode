from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach 2
        odds = sum([i & 1 for i in Counter(s).values()])
        return len(s) - odds + bool(odds)

        # Approach 1
        # res, one, d = 0, 0, {}
        # for i in s: d[i] = d[i]+1 if i in d else 1
        # for i in set(s):
        #     if d[i]&1==0: res += d[i]
        #     else: one, res = 1, res + d[i] - 1
        # return res + one
