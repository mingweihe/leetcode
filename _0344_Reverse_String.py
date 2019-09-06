class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach 2
        return s[::-1]

        # Approach 1
        # return ''.join(reversed(list(s)))
