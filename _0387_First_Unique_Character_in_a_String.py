import string


class Solution(object):

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach 1
        return min([s.index(i) for i in string.ascii_lowercase if s.count(i) == 1] or [-1])
        # Approach 2
        # d = {}
        # for i in s:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1
        # l = None
        # for i in range(len(s)):
        #     if s[i] in d and d[s[i]] == 1: return i
        # return -1
