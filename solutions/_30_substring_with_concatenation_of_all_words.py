import collections


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        if not s or not words:
            return res
        cnt = collections.Counter(words)
        n, m = len(words), len(words[0])
        for i in xrange(len(s)-m*n+1):
            _cnt = cnt.copy()
            j, k = i, n
            while k:
                cur = s[j:j+m]
                if cur not in _cnt or _cnt[cur] == 0:
                    break
                _cnt[cur] -= 1
                j += m
                k -= 1
            if k == 0: res.append(i)
        return res
