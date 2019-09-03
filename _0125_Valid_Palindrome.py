import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return re.sub('\W', '', s).lower() == (re.sub('\W', '', s))[-1::-1].lower()
