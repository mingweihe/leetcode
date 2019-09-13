class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Approach 2
        res, ind1, ind2 = len(words), -1, -1
        for i, w in enumerate(words):
            if w == word1: ind1 = i
            if w == word2:
                if word1 == word2:
                    ind1 = ind2
                ind2 = i
            if ind1 != -1 and ind2 != -1:
                res = min(res, abs(ind1-ind2))
        return res
        
        # Approach 1
        # res, ind1, ind2 = len(words), -1, -1
        # for i, w in enumerate(words):
        #     if word1 != word2:
        #         if w == word1: ind1 = i
        #         elif w == word2: ind2 = i
        #     elif w == word1:
        #         ind1, ind2 = max(ind1, ind2), i
        #     if ind1 != -1 and ind2 != -1:
        #         res = min(res, abs(ind1-ind2))
        # return res
