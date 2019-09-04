class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach 1
        return s[::-1]
        # Approach 2
        # return ''.join(reversed(list(s)))
