class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Approach 4, KMP O(n)
        if not needle: return 0
        def build(s):
            nex = [0, 0]
            j = 0
            for i in xrange(1, len(s)):
                while j > 0 and s[i] != s[j]:
                    j = nex[j]
                if s[i] == s[j]:
                    j += 1
                nex += j,
            return nex
    
        nex = build(needle)
        j = 0
        for i in xrange(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = nex[j]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1

        # Approach 3
        # return haystack.find(needle)

        # Approach 2
        # if needle in haystack: return haystack.index(needle)
        # return -1

        # Approach 1
        # if needle == '': return 0
        # l1, l2 = len(haystack), len(needle)
        # scale = l1 - l2 + 1
        # for i in range(scale):
        #     if haystack[i:i + l2] == needle:
        #         return i
        # return -1
