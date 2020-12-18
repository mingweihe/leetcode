class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach 2
        return 2 - (s == s[::-1]) - (not s)
        # Approach 1
        # if not s: return 0
        # if s == s[::-1]: return 1
        # return 2
