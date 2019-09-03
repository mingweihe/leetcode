import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        implicit BFS -> breadth first search
        """
        L, ws = len(beginWord), set(wordList)
        ws.discard(beginWord)
        queue = [(beginWord, 1)]
        while queue:
            word, level = queue.pop(0)
            if word == endWord: return level
            for i in xrange(L):
                before, after = word[:i], word[i+1:]
                for letter in string.ascii_lowercase:
                    new_word = before + letter + after
                    if new_word in ws:
                        ws.discard(new_word)
                        queue.append((new_word, level+1))
        return 0
