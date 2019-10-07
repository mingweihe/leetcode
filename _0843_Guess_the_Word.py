# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """
import itertools
import collections


class Solution(object):
    def findSecretWord(self, wordlist, master):
        # Approach 3, time O(n^2)
        n = 0
        while n < 6:
            perms = itertools.permutations(wordlist, 2)
            # the secret word has 80 percent probability appearing in the '0' family
            # coz' (25./26) ** 6 == .79
            cnts = collections.Counter(x for x, y in perms if self.match(x, y) == 0)
            # min number of 0 means max number of non-zero with other words
            # also means having a good representation of this subset
            word = min(wordlist, key=lambda w: cnts[w])
            n = master.guess(word)
            wordlist = [w for w in wordlist if self.match(w, word) == n]

        # Approach 2, O(n^2), not stable

    #         def entropy(data):
    #             summ = sum(data)
    #             data = [float(x) / summ for x in data]
    #             return -sum(prob*math.log(prob) for prob in data)

    #         def pick_word(words, tree):
    #             max_entropy = -1
    #             res = ''
    #             for word in words:
    #                 if entropy(len(tree[word][d]) for d in tree[word]) > max_entropy:
    #                     res = word
    #             return res
    #         dists = collections.defaultdict(int)
    #         for x in wordlist:
    #             for y in wordlist:
    #                 if x == y: continue
    #                 dists[x, y] = self.match(x, y)
    #         n = 0
    #         wordlist = set(wordlist) # no difference by changing to list, while got WA
    #         while n < 6:
    #             tree = collections.defaultdict(lambda:collections.defaultdict(set))
    #             # print len(wordlist)
    #             for x in wordlist:
    #                 for y in wordlist:
    #                     if x == y: continue
    #                     pre = len(tree[x][dists[x, y]])
    #                     tree[x][dists[x, y]].add(y)
    #             word = pick_word(wordlist, tree)
    #             n = master.guess(word)
    #             wordlist = tree[word][n]

    # Approach 1 time O(n), but not stable
    # n = 0
    # while n < 6:
    #     word = random.choice(wordlist)
    #     n = master.guess(word)
    #     wordlist = [w for w in wordlist if self.match(word, w) == n]

    def match(self, w1, w2):
        return len([1 for c1, c2 in zip(w1, w2) if c1 == c2])
