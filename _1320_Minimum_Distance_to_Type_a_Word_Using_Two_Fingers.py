from functools import lru_cache


class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Approach 4 time: O(26*n)
        save, res = 0, 0

        def dist(id1, id2):
            return abs(id1 / 6 - id2 / 6) + abs(id1 % 6 - id2 % 6)

        dp = [0] * 26
        for i in xrange(len(word) - 1):
            b, c = ord(word[i]) - 65, ord(word[i + 1]) - 65
            for a in xrange(26):
                dp[b] = max(dp[b], dp[a] + dist(b, c) - dist(a, c))
            save = max(save, dp[b])
            res += dist(b, c)
        return res - save
        # Approach 3 time O(52*n) kind of BFS / DP solution
        # dp2: all possibilities of current step, dp: all possibilities of last step
        # key[0]: res of left finger, key[1]: res of right finger
        # maximum range of inner loop is 26+26,  minimum range is 1
        # so the time complexity is approximately O(26*n)
        # def dist(id1, id2):
        #     if id1 == -1: return 0
        #     return abs(id1 / 6 - id2 / 6) + abs(id1 % 6 - id2 % 6)
        #
        # dp, dp2 = {(-1, ord(word[0])-65): 0}, {}
        # for c in [ord(c)-65 for c in word[1:]]:
        #     for a, b in dp:
        #         dp2[c, b] = min(dp2.get((c, b), 2700), dp[a, b] + dist(a, c))
        #         dp2[a, c] = min(dp2.get((a, c), 2700), dp[a, b] + dist(b, c))
        #     dp, dp2 = dp2, {}
        # return min(dp.values())

        # Approach 2 Optimized search, O(2^n)
        # transits = ''.join([a for a, b in zip(word, word[1:] + ' ') if a != b])
        # locations = {c: divmod(ord(c)-65, 6)for c in string.ascii_uppercase}
        # memcache = dict()
        # def dist(c1, c2):
        #     if not c1 or not c2: return 0
        #     x1, y1 = locations[c1]
        #     x2, y2 = locations[c2]
        #     return abs(x1-x2) + abs(y1-y2)

        # def search(i, char_l=None, char_r=None):
        #     if (i, char_l, char_r) in memcache: return memcache[i, char_l, char_r]
        #     if i == len(transits): return 0
        #     d1 = dist(char_l, transits[i]) + search(i+1, transits[i], char_r)
        #     d2 = dist(char_r, transits[i]) + search(i+1, char_l, transits[i])
        #     ans = min(d1, d2)
        #     memcache[i, char_l, char_r] = ans
        #     return ans
        # return search(0)

        # Approach 1 naive search, O(2^n) refer to python3 lru_cache
        # @lru_cache(None)
        # def dist(c1, c2):
        #     x1, y1 = divmod(ord(c1) - 65, 6)
        #     x2, y2 = divmod(ord(c2) - 65, 6)
        #     return abs(x1 - x2) + abs(y1 - y2)
        #
        # @lru_cache(None)
        # def search(i, j):
        #     if len(word) - 1 in (i, j): return 0
        #     next_step = max(i, j) + 1
        #     ans_i = search(next_step, j) + dist(word[i], word[next_step])
        #     ans_j = search(i, next_step)
        #     if j != -1: ans_j += dist(word[j], word[next_step])
        #     return min(ans_i, ans_j)
        #
        # return search(0, -1)
