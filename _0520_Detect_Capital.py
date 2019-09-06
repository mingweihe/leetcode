import re


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # Approach 3
        return re.compile("^([A-Z]+|[A-Z]?[a-z]+)$").match(word) is not None

        # Approach 2
        # return word.isupper() or word.islower() or word.istitle()

        # Approach 1
        # return word[1:] == word[1:].lower() or word.upper() == word
