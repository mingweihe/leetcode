class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach 2
        return ' '.join(s.split()[::-1])

        # Approach 1
        #  step 1. reverse whole string
        #  step 2. reverse each word

