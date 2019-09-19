import collections


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # Approach 2 one loop
        dic = collections.defaultdict(int)
        bulls, cows = 0, 0
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                if dic[g] > 0: cows += 1
                if dic[s] < 0: cows += 1
                dic[s] += 1
                dic[g] -= 1
        return '{}A{}B'.format(bulls, cows)

        # Approach 1 two loops
        # bulls, cows = 0, 0
        # dic = collections.Counter(guess)
        # for i in xrange(len(secret)):
        #     if secret[i] == guess[i]:
        #         bulls += 1
        #         if dic[secret[i]] != 0:
        #             dic[secret[i]] -= 1
        # for i in xrange(len(guess)):
        #     if secret[i] != guess[i] and dic[secret[i]]:
        #         cows += 1
        #         dic[secret[i]] -= 1
        # return `bulls`+'A'+`cows`+'B'
