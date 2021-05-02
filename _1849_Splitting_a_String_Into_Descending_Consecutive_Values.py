class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def dfs(idx, pre):
            if idx == len(s): return True
            for i in xrange(idx, len(s)):
                cur = int(s[idx:i+1])
                if cur != pre - 1: continue
                if dfs(i+1, cur): return True
            return False
        if len(s) == 1: return False
        for i in xrange(1, len(s)):
            if dfs(i, int(s[:i])): return True
        return False
