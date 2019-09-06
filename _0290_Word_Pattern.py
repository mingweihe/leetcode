class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # Approach 2
        return list(map(pattern.find, pattern)) == list(map(str.split().index, str.split()))

        # Approach 1
        # d = {}
        # a1, a2 = list(pattern), str.split(' ')
        # if len(a1) != len(a2): return False
        # for i in range(len(a1)):
        #     if a1[i] in d:
        #         if d[a1[i]] != a2[i]: return False
        #     else:
        #         if a2[i] in d.values(): return False
        #         d[a1[i]] = a2[i]
        # return True
