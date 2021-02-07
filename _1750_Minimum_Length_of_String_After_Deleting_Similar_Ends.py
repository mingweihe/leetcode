class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            while l+1 < r and s[l] == s[l+1]: l += 1
            while r-1 > l and s[r] == s[r-1]: r -= 1
            if r > l: l, r = l+1, r-1
            else: break
        return r-l+1
