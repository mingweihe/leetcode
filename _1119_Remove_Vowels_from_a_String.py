import re


class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        return re.sub('a|e|i|o|u', '', S)
