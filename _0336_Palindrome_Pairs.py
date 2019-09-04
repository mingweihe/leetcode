class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res, d = [], {w[::-1]: i for i, w in enumerate(words)}
        for i, w in enumerate(words):
            for j in xrange(len(w)):
                left, right = w[:j], w[j:]
                if left in d and i != d[left] and right == right[::-1]:
                    res.append([i, d[left]])
                    if not left: res.append([d[left], i])
                if right in d and i != d[right] and left == left[::-1]:
                    res.append([d[right], i])
        return res
