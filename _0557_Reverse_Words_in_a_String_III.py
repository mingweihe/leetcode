class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Approach 1
        # return ' '.join(i[::-1] for i in s.split())
        # Approach 2
        return ' '.join(s.split()[::-1])[::-1]
