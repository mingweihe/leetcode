from collections import Counter


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
