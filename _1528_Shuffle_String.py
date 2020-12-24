class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = [None] * len(s)
        for i, x in enumerate(indices):
            res[x] = s[i]
        return ''.join(res)
