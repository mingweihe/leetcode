from collections import Counter


class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        cnts = Counter(word)
        arr = sorted(cnts.values())
        res = len(word)
        pre = 0
        for i in xrange(len(arr)):
            cur = 0
            for j in xrange(i + 1, len(arr)):
                cur += max(abs(arr[i] - arr[j]) - k, 0)
            res = min(res, cur + pre)
            pre += arr[i]
        return res
