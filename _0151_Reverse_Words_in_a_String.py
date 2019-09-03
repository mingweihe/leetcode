class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach 1
        return ' '.join(s.split()[::-1])
        # Approach 2
        #  step 1. reverse whole string
        #  step 2. reverse each word

