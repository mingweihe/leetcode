class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Approach 2 O(n)
        res, ind1, ind2 = len(words), -1, -1
        for i,x in enumerate(words):
            if x == word1: ind1 = i
            elif x == word2: ind2 = i
            if ind1 != -1 and ind2 != -1:
                res = min(res, abs(ind1-ind2))
        return res
        
        # Approach 1 O(n^2)
        # res = len(words)
        # for i in xrange(len(words)):
        #     if words[i] == word1:
        #         for j in xrange(len(words)):
        #             if words[j] == word2:
        #                 res = min(res, abs(i-j))
        # return res
