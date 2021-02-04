from collections import Counter


class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left, right = Counter(), Counter(s)
        for c in s:
            left[c] += 1
            right[c] -= 1
            if right[c] == 0: right.pop(c)
            if len(left) == len(right): res += 1
        return res
