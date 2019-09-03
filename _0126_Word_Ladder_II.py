import collections
import string


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        layer = {beginWord: [[beginWord]]}
        L = len(beginWord)
        wordList = set(wordList)
        while layer:
            new_layer = collections.defaultdict(list)
            for w in layer:
                if w == endWord: return layer[w]
                for i in xrange(L):
                    for c in string.ascii_lowercase:
                        nw = w[:i] + c + w[i+1:]
                        if nw in wordList:
                            new_layer[nw] += [x + [nw] for x in layer[w]]
            wordList -= set(new_layer.keys())
            layer = new_layer
        return []
