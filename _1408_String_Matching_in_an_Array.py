class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for i in xrange(len(words)):
            for j in xrange(len(words)):
                if i == j: continue
                if words[i] in words[j]:
                    res += words[i],
                    break
        return res
