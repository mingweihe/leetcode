class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, cnt = 0, 0
        for c in s:
            if c == 'L': cnt += 1
            else: cnt -= 1
            res += cnt == 0
        return res
