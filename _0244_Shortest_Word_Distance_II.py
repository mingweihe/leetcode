import collections


class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dict = collections.defaultdict(list)
        for i, w in enumerate(words):
            self.dict[w].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Approach 2 O(m+n)
        res = float('inf')
        l1, l2 = self.dict[word1], self.dict[word2]
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i]-l2[j]))
            if l1[i] < l2[j]: i += 1
            else: j += 1
        return res
        # Approach 1 O(m*n)
        # res = float('inf')
        # for i in self.dict[word1]:
        #     for j in self.dict[word2]:
        #         res = min(res, abs(i-j))
        # return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
