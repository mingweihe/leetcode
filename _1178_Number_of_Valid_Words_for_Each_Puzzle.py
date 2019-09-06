import collections
import itertools


class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
            flexible using of frozenset, hashtable, combinations,
                product, compress, etc.
        """
        # Approach 2 frozenset, itertools.combinations
        words = [frozenset(word) for word in words if len(set(word)) < 8]
        cnts = collections.Counter(words)
        res = []
        for i, x in enumerate(puzzles):
            pre = x[0]
            remained = x[1:]
            cur = 0
            for j in xrange(7):
                for candidate in itertools.combinations(remained, j):
                    cur += cnts[frozenset(pre + ''.join(candidate))]
            res += [cur]
        return res

        # Approach 1 frozenset, itertools.product, itertools.compress
        # words = [frozenset(word) for word in words if len(set(word)) < 8]
        # cnts = collections.Counter(words)
        # res = []
        # for i, x in enumerate(puzzles):
        #     pre = x[0]
        #     remained = x[1:]
        #     cur = 0
        #     for selector in itertools.product([0, 1], repeat=6):
        #         candidate = itertools.compress(remained, selector)
        #         cur += cnts[frozenset(pre + ''.join(candidate))]
        #     res += [cur]
        # return res
