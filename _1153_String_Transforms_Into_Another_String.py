class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        if str1 == str2: return True
        d = dict()
        for i in xrange(len(str1)):
            if d.setdefault(str1[i], str2[i]) != str2[i]:
                return False
            # if str1[i] in d and d[str1[i]] != str2[i]: return False
            # d[str1[i]] = str2[i]
        return len(set(str2)) != 26
