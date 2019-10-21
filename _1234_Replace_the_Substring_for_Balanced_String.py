import collections


class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        solution: sliding window
        time O(n) space O(1)
        """
        cnt = collections.Counter(s)
        res = n = len(s)
        i, avg = 0, n / 4
        for j, c in enumerate(s):
            cnt[c] -= 1
            while i < n and all(cnt[x] <= avg for x in 'QWER'):
                res = min(res, j-i+1)
                cnt[s[i]] += 1
                i += 1
        return res
