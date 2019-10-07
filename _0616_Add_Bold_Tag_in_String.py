class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
            trick: problem transformation for string
            time O(n*k*n) space O(n)
        """
        L = len(s)
        bolds = [False] * L
        end = 0
        for i in xrange(L):
            for ds in dict:
                if s.startswith(ds, i):
                    end = max(end, i + len(ds))
            bolds[i] = end > i
        res, i = '', 0
        while i < L:
            if not bolds[i]:
                res += s[i]
                i += 1
                continue
            j = i + 1
            while j < L and bolds[j]: j += 1
            res += '<b>' + s[i:j] + '</b>'
            i = j
        return res
