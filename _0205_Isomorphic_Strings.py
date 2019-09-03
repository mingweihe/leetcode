class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1, dic2 = {}, {}
        if len(s) != len(t): return False
        s, t = list(s), list(t)
        for i in range(len(s)):
            if s[i] in dic1:
                if not t[i] in dic2: return False
                if dic1[s[i]] != dic2[t[i]]: return False
            elif t[i] in dic2:
                if not s[i] in dic1: return False
                if dic1[s[i]] != dic2[t[i]]: return False
            else: dic1[s[i]] = dic2[t[i]] = i
        return True
