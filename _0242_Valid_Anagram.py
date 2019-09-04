class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Approach 1
        # return sorted(s) == sorted(t)
        # Approach 2
        if not len(s) == len(t):
            return False
        dic, dic1 = {}, {}
        for i in range(len(s)):
            if not s[i] in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
            if not t[i] in dic1:
                dic1[t[i]] = 1
            else:
                dic1[t[i]] += 1
        return dic == dic1
