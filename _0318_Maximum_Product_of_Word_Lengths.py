class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
            encoding + bit manipulation
            time O(n^2) space O(n)
        """
        L = len(words)
        bytes = [0]*L
        for i, w in enumerate(words):
            for c in w:
                bytes[i] |= 1 << ord(c) - 97
        res = 0
        for i in xrange(L-1):
            for j in xrange(i+1, L):
                if bytes[i] & bytes[j] == 0:
                    res = max(res, len(words[i])*len(words[j]))
        return res
