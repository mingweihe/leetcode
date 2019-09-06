class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
            sliding window
        """
        start = end = 0
        res = 0
        L = len(s)
        dic = {}
        while end < L:
            if len(dic) < 3:
                dic[s[end]] = end
                end += 1
            if len(dic) == 3:
                left_most = min(dic.values())
                start = left_most + 1
                dic.pop(s[left_most])
            res = max(res, end-start)
        return res
