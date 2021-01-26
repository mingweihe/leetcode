from collections import Counter


class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = Counter(s)
        res = []
        keys = sorted(cnt.keys())
        while len(res) != len(s):
            for k in keys:
                if cnt[k] > 0:
                    res += k,
                    cnt[k] -= 1
            for i in xrange(len(keys)-1, -1, -1):
                k = keys[i]
                if cnt[k] > 0:
                    res += k,
                    cnt[k] -= 1
        return ''.join(res)
