class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ''
        common = strs[0]
        for i in range(1, len(strs)):
            common = self.commonInTwo(common, strs[i])
        return common

    def commonInTwo(self, s1, s2):
        for i, c in enumerate(s1):
            if i == len(s2) or c != s2[i]:
                return s1[:i]
        return s1
