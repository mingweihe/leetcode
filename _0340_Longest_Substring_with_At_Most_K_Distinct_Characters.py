class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        d = {}
        cnt = 0
        res = 0
        for i in xrange(len(s)):
            if s[i] not in d:
                cnt += 1
            d[s[i]] = i
            if cnt <= k:
                res = max(res, i - left + 1)
            else:
                if d[s[left]] == left:
                    d.pop(s[left])
                    cnt -= 1
                left += 1
        return res
