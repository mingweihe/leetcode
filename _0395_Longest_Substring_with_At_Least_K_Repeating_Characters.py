from collections import Counter


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for c, cnt in Counter(s).items():
            if cnt >= k: continue
            ans = float('-inf')
            for ss in s.split(c):
                ans = max(ans, self.longestSubstring(ss, k))
            return ans
        return len(s)
