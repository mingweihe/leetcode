class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Approach 3
        return haystack.find(needle)

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
