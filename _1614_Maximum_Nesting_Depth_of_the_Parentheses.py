class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur, res = 0, 0
        for c in s:
            if c not in ('(', ')'):
                continue
            if c == ')':
                res = max(res, cur)
                cur -= 1
            else:
                cur += 1
        return res
