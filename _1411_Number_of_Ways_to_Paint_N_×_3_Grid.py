class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## Approach 2
        a121, a123, mod = 6, 6, 10**9 + 7
        for _ in xrange(n-1):
            a121, a123 = a121 * 3 + a123 * 2, a121 * 2 + a123 * 2
        return (a121 + a123) % mod

        ## Approach 1
        # MOD = 10**9 + 7
        # colors = [
        #     [0, 1, 0], [1, 0, 1], [2, 0, 1],
        #     [0, 1, 2], [1, 0, 2], [2, 0, 2],
        #     [0, 2, 0], [1, 2, 0], [2, 1, 0],
        #     [0, 2, 1], [1, 2, 1], [2, 1, 2]
        # ]
        # res = 0
        # last = [[-1, -1, -1, 1]]
        # for i in xrange(n):
        #     counter = [0] * 12
        #     for x, y, z, cnt in last:
        #         for i, (a, b, c) in enumerate(colors):
        #             if a != x and b != y and c != z:
        #                 counter[i] += cnt
        #     last = []
        #     for i, x in enumerate(counter):
        #         if x == 0: continue
        #         last += colors[i] + [x],
        # return sum(x[3] for x in last) % MOD
